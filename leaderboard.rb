require 'rubygems'
require 'nokogiri'
require 'open-uri'
require 'fileutils'
BASE_URL = 'http://karmalb.com'
BASE_DIR = '/user/rank%3A'
LOCAL_DIR = '/Users/lanxihuang/buddy/data/leadership2'

FileUtils.makedirs(LOCAL_DIR) unless File.exists?LOCAL_DIR

# get metainfo from first page:
page = Nokogiri::HTML(open(BASE_URL+BASE_DIR + '1'))

# write the HTML for page 1 to disk
File.open("#{LOCAL_DIR}/1.html", 'w'){|f| f.write(page.to_html)}

last_page_number = 1325001
#page.css("a.end.lastLink.button")[0]['href'].match(/page=(\d+)/)[1].to_i

puts "Iterating from 11 to #{last_page_number}"

pg_number = 11
while pg_number <= 1325001 do
  puts "Getting #{pg_number}"
  File.open("#{LOCAL_DIR}/#{pg_number}.html", 'w') do |f| 
    f.write( open("#{BASE_URL}#{BASE_DIR}#{pg_number}").read )
  end
  pg_number += 10
end
