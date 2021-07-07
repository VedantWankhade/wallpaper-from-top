from wordcloud import WordCloud


def generate_wordcloud(word_frequency_mapping, width=1920, height=1080, background_color='black'):
    wc = WordCloud(
        background_color=background_color,
        width=width,
        height=height).generate_from_frequencies(word_frequency_mapping)

    return wc
