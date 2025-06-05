window.localStorageInterop = {
    get: function (key) {
        return window.localStorage.getItem(key);
    },
    set: function (key, data) {
        window.localStorage.setItem(key, data);
    }
};
