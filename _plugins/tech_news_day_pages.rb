# frozen_string_literal: true

module Jekyll
  # Generator for creating individual day pages for tech news
  class TechNewsDayPages < Generator
    safe true
    priority :lowest

    def generate(site)
      return unless site.collections.key?('tech_news')

      tech_news = site.collections['tech_news'].docs
      return if tech_news.empty?

      # Group articles by date
      articles_by_date = tech_news.group_by { |article|
        article.date.strftime('%Y-%m-%d')
      }

      # Create a page for each date
      articles_by_date.each do |date_string, articles|
        # Skip if we already have a page for this date
        existing_page = site.pages.find { |page|
          page.url == "/tech-news/#{date_string}/"
        }

        next if existing_page

        # Create new page
        page = TechNewsDayPage.new(site, site.source, '', date_string)
        site.pages << page

        Jekyll.logger.info "Tech News Day Pages:", "Generated page for #{date_string} (#{articles.size} articles)"
      end
    end
  end

  # Page class for individual day pages
  class TechNewsDayPage < Page
    def initialize(site, base, dir, date_string)
      @site = site
      @base = base
      @dir = dir
      @name = "#{date_string}.html"

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tech_news_day.html')

      # Set page data
      self.data['layout'] = 'tech_news_day'
      self.data['title'] = "Technologické zprávy - #{Date.parse(date_string).strftime('%d.%m.%Y')}"
      self.data['date'] = date_string
      self.data['permalink'] = "/tech-news/#{date_string}/"

      # Add description with date
      parsed_date = Date.parse(date_string)
      self.data['description'] = "Technologické zprávy z #{parsed_date.strftime('%d.%m.%Y')} - automaticky přeložené a vyhodnocené podle důležitosti."
    end
  end
end