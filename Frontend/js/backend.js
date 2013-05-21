// Generated by IcedCoffeeScript 1.4.0c
(function() {
  var Backend, Resource, iced, __iced_k, __iced_k_noop,
    __slice = [].slice;

  iced = {
    Deferrals: (function() {

      function _Class(_arg) {
        this.continuation = _arg;
        this.count = 1;
        this.ret = null;
      }

      _Class.prototype._fulfill = function() {
        if (!--this.count) return this.continuation(this.ret);
      };

      _Class.prototype.defer = function(defer_params) {
        var _this = this;
        ++this.count;
        return function() {
          var inner_params, _ref;
          inner_params = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
          if (defer_params != null) {
            if ((_ref = defer_params.assign_fn) != null) {
              _ref.apply(null, inner_params);
            }
          }
          return _this._fulfill();
        };
      };

      return _Class;

    })(),
    findDeferral: function() {
      return null;
    },
    trampoline: function(_fn) {
      return _fn();
    }
  };
  __iced_k = __iced_k_noop = function() {};

  Resource = (function() {

    function Resource(api_endpoint_url, backend) {
      this.api_endpoint_url = api_endpoint_url;
      this.backend = backend;
    }

    Resource.prototype.get = function(filters, callback) {
      var response, ___iced_passed_deferral, __iced_deferrals, __iced_k,
        _this = this;
      __iced_k = __iced_k_noop;
      ___iced_passed_deferral = iced.findDeferral(arguments);
      if (filters == null) filters = {};
      (function(__iced_k) {
        __iced_deferrals = new iced.Deferrals(__iced_k, {
          parent: ___iced_passed_deferral,
          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/backend.iced",
          funcname: "Resource.get"
        });
        backend.get(_this.api_endpoint_url, filters, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return response = arguments[0];
            };
          })(),
          lineno: 7
        }));
        __iced_deferrals._fulfill();
      })(function() {
        return callback(response.objects);
      });
    };

    Resource.prototype["delete"] = function(id, callback) {
      return backend["delete"]("" + this.api_endpoint_url + id + "/", callback);
    };

    Resource.prototype.create = function(object, callback) {
      var response, ___iced_passed_deferral, __iced_deferrals, __iced_k,
        _this = this;
      __iced_k = __iced_k_noop;
      ___iced_passed_deferral = iced.findDeferral(arguments);
      if (object == null) object = {};
      (function(__iced_k) {
        __iced_deferrals = new iced.Deferrals(__iced_k, {
          parent: ___iced_passed_deferral,
          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/backend.iced",
          funcname: "Resource.create"
        });
        backend.post(_this.api_endpoint_url, object, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return response = arguments[0];
            };
          })(),
          lineno: 14
        }));
        __iced_deferrals._fulfill();
      })(function() {
        return callback(response.responseJSON);
      });
    };

    Resource.prototype.update = function(id, options, callback) {
      return backend.put("" + this.api_endpoint_url + id + "/", options, callback);
    };

    return Resource;

  })();

  Backend = (function() {

    function Backend(server_url) {
      this.server_url = server_url;
      this.Bottle = new Resource("/api/v1/bottle/");
      this.Cellar = new Resource("/api/v1/cellar/");
      this.Winery = new Resource("/api/v1/winery/");
      this.Wine = new Resource("/api/v1/wine/");
      this.Annotation = new Resource("/api/v1/annotation/");
      this.Sommeilier = new Resource("/api/v1/sommeilier/");
      this.Profile = new Resource("/api/v1/profile/");
      this.userId = this.getUserCookie();
      this.profileUri = "/api/v1/profile/" + this.userId + "/";
    }

    Backend.prototype.isGood = function(response) {
      return response.status === 304 || parseInt(response.status / 100) === 2;
    };

    Backend.prototype.get = function(uri, options, callback) {
      return $.get(this.server_url + uri, options, callback);
    };

    Backend.prototype.post = function(uri, data, callback) {
      return $.ajax({
        url: this.server_url + uri,
        contentType: "application/json",
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        processData: false,
        complete: callback
      });
    };

    Backend.prototype.put = function(uri, data, callback) {
      return $.ajax({
        url: this.server_url + uri,
        contentType: "application/json",
        type: "PUT",
        data: JSON.stringify(data),
        dataType: "json",
        processData: false,
        complete: callback
      });
    };

    Backend.prototype["delete"] = function(uri, callback) {
      return $.ajax({
        url: this.server_url + uri,
        type: "DELETE",
        complete: callback,
        dataType: "json"
      });
    };

    Backend.prototype.login = function(email, password, success, failure) {
      var account, response, ___iced_passed_deferral, __iced_deferrals, __iced_k,
        _this = this;
      __iced_k = __iced_k_noop;
      ___iced_passed_deferral = iced.findDeferral(arguments);
      account = {
        "username": email,
        "password": password
      };
      (function(__iced_k) {
        __iced_deferrals = new iced.Deferrals(__iced_k, {
          parent: ___iced_passed_deferral,
          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/backend.iced",
          funcname: "Backend.login"
        });
        _this.post("/api/v1/auth/user/login/", account, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return response = arguments[0];
            };
          })(),
          lineno: 73
        }));
        __iced_deferrals._fulfill();
      })(function() {
        if (_this.isGood(response)) {
          _this.setUserCookie(response.responseJSON.userId);
          return success(response.responseJSON);
        } else {
          return failure();
        }
      });
    };

    Backend.prototype.logout = function() {
      return this.removeUserCookie();
    };

    Backend.prototype.createUserAccount = function(name, email, password, success, failure) {
      var account, response, ___iced_passed_deferral, __iced_deferrals, __iced_k,
        _this = this;
      __iced_k = __iced_k_noop;
      ___iced_passed_deferral = iced.findDeferral(arguments);
      account = {
        "name": name,
        "email": email,
        "password": password
      };
      (function(__iced_k) {
        __iced_deferrals = new iced.Deferrals(__iced_k, {
          parent: ___iced_passed_deferral,
          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/backend.iced",
          funcname: "Backend.createUserAccount"
        });
        _this.post("/api/v1/profile/", account, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return response = arguments[0];
            };
          })(),
          lineno: 92
        }));
        __iced_deferrals._fulfill();
      })(function() {
        if (_this.isGood(response)) {
          _this.setUserCookie(response.responseJSON.id);
          return success(response.responseJSON);
        } else {
          return failure();
        }
      });
    };

    Backend.prototype.setUserCookie = function(userId) {
      return $.cookie("userId", userId);
    };

    Backend.prototype.getUserCookie = function() {
      return parseInt($.cookie("userId"));
    };

    Backend.prototype.removeUserCookie = function() {
      return $.removeCookie("userId");
    };

    Backend.prototype.userIsLoggedIn = function() {
      return !!($.cookie("userId"));
    };

    return Backend;

  })();

  window.backend = new Backend("http://localhost:8000");

}).call(this);
