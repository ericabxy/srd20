NAME = 'New Post'

install:
	bundle config set --local path 'vendor/bundle'
	bundle install

run: 
	bundle exec jekyll serve

%.markdown: %.rtf
	pandoc --standalone -f rtf -t markdown_phpextra+pipe_tables -o $@ $<

post:
	bundle exec jekyll compose $(NAME)

clean:
	bundle exec jekyll clean
