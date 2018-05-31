package main

import (
	"fmt"
	"github.com/anaskhan96/soup"
	"os"
	"strconv"
	"strings"
)

func main() {
	GetSearchPage()
}

func GetSearchPage() {
	base_url := "http://nccardinal.org"
	library_number := 132
	search_url := "/eg/opac/results?bool=and&qtype=keyword&contains=contains&query=&bool=and&qtype=title&contains=contains&query=&bool=and&qtype=author&contains=contains&query=&_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=" + strconv.Itoa(library_number) + "&pubdate=is&date1=&date2=&sort=pubdate.descending"
	url := base_url + search_url
	fmt.Println("url:", url)
		
	resp, err := soup.Get(url)
	if err != nil {
		os.Exit(1)
	}
	
	doc := soup.HTMLParse(resp)
	links := doc.FindAll("a", "class", "record_title search_link")
	fmt.Println(links)
	
	for _, link := range links {
		// fmt.Println(link.Text(), "| Link :", link.Attrs()["href"]) 
		fmt.Println(strings.TrimSpace(strings.Split(link.Text(), "[videorecording]")[0]))
	}
}
