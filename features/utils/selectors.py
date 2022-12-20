import enum

class Selectors():

    all_movies_btn_xpath = '/html/body/main/nav/div/a[1]'
    sort_by_default_xpath = '/html/body/main/ul/li[1]/a'
    sort_by_date_xpath = '/html/body/main/ul/li[2]/a'
    show_more_btn_xpath = '/html/body/main/section[1]/section[1]/button'
    close_film_card_xpath = '/html/body/section/form/div[1]/div[1]/button'
    film_list_xpath = '/html/body/main/section[1]/section[1]/div'

    film_card_preview_css_class = '.film-card__poster'
    film_card_release_date_css_class = '.film-card__year'
    film_card_duration_css_class = '.film-card__duration'
    film_card_genre_css_class = '.film-card__genre'
    film_card_title_css_class = '.film-card__title'
    film_card_comment_count = '.film-card__comments'

    main_btn_active_class = ".main-navigation__item--active"

    film_card_class = {
        "poster": ".film-card__poster",
        "release_date": ".film-card__year",
        "title": ".film-card__title",
        "comments": ".film-card__comments",
        "details": ".film-details"
    }

    filtration_btn_xpath = {
        "watchlist": "/html/body/main/nav/div/a[2]",
        "history": "/html/body/main/nav/div/a[3]",
        "favorites": "/html/body/main/nav/div/a[4]"
    }
