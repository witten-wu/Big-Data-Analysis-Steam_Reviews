from Filter import ReFilter, CommentFilter, TokenFilter, VectorFilter, CoordinatesFilter


class Pipe:
    def __init__(self, stop_words_path, pattern, vec_para, lsa_para, userdict=None):
        self.filters = []
        self.filters.append(ReFilter(pattern))
        self.filters.append(CommentFilter(userdict))
        self.filters.append(TokenFilter(stop_words_path))
        self.filters.append(VectorFilter(vec_para))
        self.filters.append(CoordinatesFilter(lsa_para))

    def invoke(self, raw_data):
        token = []
        length = len(raw_data)
        for i in range(length):
            data = raw_data.iloc[i] # 取第i行
            for f in self.filters[:3]:
                data = f.invoke(data)
            token.append(" ".join(data))
        X, terms = self.filters[3].invoke(token)
        X_topics, coordinates = self.filters[4].invoke(X)
        return token, X_topics, coordinates, terms
