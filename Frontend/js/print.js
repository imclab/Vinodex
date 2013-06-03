// Generated by IcedCoffeeScript 1.4.0c
(function() {
  var iced, __iced_k, __iced_k_noop,
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

  $(function() {
    var bottle_ids, bottles, html, user, ___iced_passed_deferral, __iced_deferrals, __iced_k,
      _this = this;
    __iced_k = __iced_k_noop;
    ___iced_passed_deferral = iced.findDeferral(arguments);
    bottle_ids = JSON.parse($.cookie('toprint'));
    bottles = [];
    (function(__iced_k) {
      __iced_deferrals = new iced.Deferrals(__iced_k, {
        parent: ___iced_passed_deferral,
        filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/print.iced"
      });
      if (!bottle_ids.length) {
        backend.Bottle.get({
          cellar__owner: backend.userId
        }, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return bottles = arguments[0];
            };
          })(),
          lineno: 6
        }));
      } else {
        backend.Bottle.getByIds(bottle_ids.join(";"), __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return bottles = arguments[0];
            };
          })(),
          lineno: 9
        }));
      }
      backend.Profile.getById(backend.userId, __iced_deferrals.defer({
        assign_fn: (function() {
          return function() {
            return user = arguments[0];
          };
        })(),
        lineno: 11
      }));
      __iced_deferrals._fulfill();
    })(function() {
      (function(__iced_k) {
        __iced_deferrals = new iced.Deferrals(__iced_k, {
          parent: ___iced_passed_deferral,
          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/print.iced"
        });
        frontend.renderTemplate("print", {
          bottles: bottles,
          name: user.name
        }, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return html = arguments[0];
            };
          })(),
          lineno: 12
        }));
        __iced_deferrals._fulfill();
      })(function() {
        $("body").html(html);
        return $(window).bind("load", function() {
	       window.print(); 
        });
      });
    });
  });

}).call(this);
