package main

import (
	"fmt"
	"github.com/anaskhan96/soup"
	"net/http"
	//"io/ioutil"
	"encoding/json"
	"os"
	"strconv"
	"strings"
	"time"
)

type TitleSearchResult struct {
	Query string
	Results []TitleResult
}

type TitleResult struct {
	Name, Description, Url []string
}

func main() {
	// titles := getSearchPage()
	// fmt.Println("titles:", titles)

	// for _, title := range titles {
	// 	// TODO:as create Go Routines for getting information for each title.
	// }

	getMovieInfo()
}

func getSearchPage() []string {
	base_url := "http://nccardinal.org"
	library_number := 132
	search_url := "/eg/opac/results?bool=and&qtype=keyword&contains=contains&query=&bool=and&qtype=title&contains=contains&query=&bool=and&qtype=author&contains=contains&query=&_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=" + strconv.Itoa(library_number) + "&pubdate=is&date1=&date2=&sort=pubdate.descending"
	url := base_url + search_url
	//fmt.Println("url:", url)
		
	resp, err := soup.Get(url)
	if err != nil {
		os.Exit(1)
	}
	
	doc := soup.HTMLParse(resp)
	links := doc.FindAll("a", "class", "record_title search_link")
	//fmt.Println(links)

	// TODO:as also get the library link for each movie.
	
	titles := make([]string, len(links))
	
	for _, link := range links {
		// fmt.Println(link.Text(), "| Link :", link.Attrs()["href"]) 
		//fmt.Println(strings.TrimSpace(strings.Split(link.Text(), "[videorecording]")[0]))
		titles = append(titles, strings.TrimSpace(strings.Split(link.Text(), "[videorecording]")[0]))
	}
	
	return titles
}

func getMovieInfo() {
	title := "The Post"

	searchUrl := "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search="

	//searchRes := TitleSearchResult{}
	var model []interface{}
	getJson(searchUrl + title, &model)
}

var myClient = &http.Client{Timeout: 10 * time.Second}

func getJson(url string, target interface{}) error {
    r, err := myClient.Get(url)
    if err != nil {
        return err
    }
	defer r.Body.Close()

	if err := json.Unmarshal([]byte(r.Body), target); err != nil {
		fmt.Println("err:", err)
	}
	//	fmt.Println("searchRes:", model)
	for _, x := range model {
		switch value := x.(type) {
		case string:
			fmt.Println(value)
		case []interface{}:
			for _, v := range value {
				fmt.Println(v.(string))
			}
		}
	}

    return json.NewDecoder(r.Body).Decode(target)
}
