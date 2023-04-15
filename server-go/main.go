package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"
	"strconv"

	pb "gdarruda.me/redis-grpc/protobufs"
	"github.com/go-redis/redis"
	"google.golang.org/grpc"
)

var (
	port   = flag.Int("port", 50052, "The server port")
	client = redis.NewClient(&redis.Options{
		Addr: "localhost:6379",
	})
)

type server struct {
	pb.UnimplementedPredictionsServer
}

func get_content(key string) *redis.StringStringMapCmd {

	key_redis := fmt.Sprintf("predictions:%v", key)
	return client.HGetAll(key_redis)

}

func (s *server) GetPredictions(ctx context.Context, in *pb.PredictionRequest) (*pb.PredictionResponse, error) {

	prediction_redis := get_content(in.GetIdClient()).Val()
	predictions := make([]*pb.Prediction, len(prediction_redis))
	i := 0

	for k, v := range prediction_redis {

		value, _ := strconv.ParseFloat(v, 32)
		float := float32(value)

		predictions[i] = &pb.Prediction{
			ClassName: k,
			Value:     float}

		i += 1

	}

	return &pb.PredictionResponse{Predictions: predictions}, nil
}

func main() {

	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterPredictionsServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())

	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
