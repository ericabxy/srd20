run: 
	bundle exec jekyll serve

install:
	bundle config set --local path 'vendor/bundle'
	bundle install

clean:
	bundle exec jekyll clean
