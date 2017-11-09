package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

// "Body"
type Body struct {
	URL  string `json:"url"`
	Code int    `json:"code"`
}

func main() {
	fmt.Printf("Hello world!")
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		response, err := json.Marshal(Body{URL: r.URL.Path, Code: 404})
		if err != nil {
			fmt.Println("JSON Marshal error:", err)
			return
		}
		fmt.Fprintf(w, "hello, %q", response)
	})
	log.Fatal(http.ListenAndServe(":8080", nil))
}
