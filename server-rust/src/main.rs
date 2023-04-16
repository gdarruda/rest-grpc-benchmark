use r2d2_redis::{r2d2::{self, PooledConnection}, RedisConnectionManager, redis::Commands};
use warp::Filter;
use std::collections::HashMap;
use std::env;

fn get_prediction(mut conn: PooledConnection<RedisConnectionManager>, 
                  key: &str) -> HashMap<String, f32> {

    let map : HashMap<String, f32> = match conn.hgetall(key) {
        Ok(m) => m,
        Err(error) => panic!("Get key error: {:?}", error)
    };

    map
}

#[tokio::main]
async fn main() {
    
    let manager = RedisConnectionManager::new("redis://127.0.0.1/").unwrap();

    let pool = r2d2::Pool::builder()
        .max_size(20)
        .build(manager)
        .unwrap();

    let redis = warp::any()
        .map(move || pool.clone().get().unwrap());


    if env::var_os("RUST_LOG").is_none() {
        // Set `RUST_LOG=todos=debug` to see debug logs,
        // this only shows access logs.
        env::set_var("RUST_LOG", "predictions=info");
    }

    let predictions = warp::path("predictions")
            .and(redis)
            .and(warp::path::param())
            .map(|conn: PooledConnection<RedisConnectionManager>, id_client: String| {
                warp::reply::json(&get_prediction(conn, 
                                                  &format!("predictions:{id_client}")))
            })
            ;
    
    let routes = warp::get()
        .and(predictions)
        .with(warp::log("predictions"));

    warp::serve(routes).run(([127, 0, 0, 1], 3031)).await;
    
}
