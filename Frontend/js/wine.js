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
    window.bottleId = parseInt(window.location.hash.substr(1));
    if (!bottleId) window.location = "/collection.html";
    $("#deleteconfirm").click(function(event) {
      var nothing, ___iced_passed_deferral, __iced_deferrals, __iced_k,
        _this = this;
      __iced_k = __iced_k_noop;
      ___iced_passed_deferral = iced.findDeferral(arguments);
      event.preventDefault();
      if ($("#deletetext").val().trim() === "DELETE") {
        (function(__iced_k) {
          __iced_deferrals = new iced.Deferrals(__iced_k, {
            parent: ___iced_passed_deferral,
            filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/wine.iced"
          });
          backend.Bottle["delete"](bottleId, __iced_deferrals.defer({
            assign_fn: (function() {
              return function() {
                return nothing = arguments[0];
              };
            })(),
            lineno: 10
          }));
          __iced_deferrals._fulfill();
        })(function() {
          return __iced_k(window.location = "/collection.html");
        });
      } else {
        return __iced_k($("#deletetext").valerror());
      }
    });
    $("a.fake").click(function(event) {
      return event.preventDefault();
    });
    window.renderPage = function() {
      var annotations, bottle, cellars, html, ___iced_passed_deferral, __iced_deferrals, __iced_k,
        _this = this;
      __iced_k = __iced_k_noop;
      ___iced_passed_deferral = iced.findDeferral(arguments);
      $(".templateContent").remove();
      (function(__iced_k) {
        __iced_deferrals = new iced.Deferrals(__iced_k, {
          parent: ___iced_passed_deferral,
          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/wine.iced",
          funcname: "renderPage"
        });
        backend.Bottle.getById(bottleId, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return bottle = arguments[0];
            };
          })(),
          lineno: 21
        }));
        backend.Cellar.get({
          owner: backend.userId
        }, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return cellars = arguments[0];
            };
          })(),
          lineno: 22
        }));
        backend.Annotation.get({
          bottle: bottleId
        }, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return annotations = arguments[0];
            };
          })(),
          lineno: 23
        }));
        __iced_deferrals._fulfill();
      })(function() {
        (function(__iced_k) {
          __iced_deferrals = new iced.Deferrals(__iced_k, {
            parent: ___iced_passed_deferral,
            filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/wine.iced",
            funcname: "renderPage"
          });
          frontend.renderTemplate("wine", {
            bottle: bottle,
            cellars: cellars,
            annotations: annotations
          }, __iced_deferrals.defer({
            assign_fn: (function() {
              return function() {
                return html = arguments[0];
              };
            })(),
            lineno: 27
          }));
          __iced_deferrals._fulfill();
        })(function() {
          $("#deletewine").before(html);
          $(".deleteannotation").click(function(event) {
            event.preventDefault();
            backend.Annotation["delete"](parseInt($(this).data('id')));
            return $(this).parents("tr").slideUp();
          });
          return $("#valaddwine").click(function(event) {
            var alcohol, bottles, cellar, name, nothing, price, type, wine, winery, wineryName, year, ___iced_passed_deferral1, __iced_deferrals, __iced_k, _bottle, _wine,
              _this = this;
            __iced_k = __iced_k_noop;
            ___iced_passed_deferral1 = iced.findDeferral(arguments);
            event.preventDefault();
            if ($("#imagefile").val() && window.FileReader) {
              if ($("#imagefile")[0].files[0].size / (1024 * 1024) > 10) {
                alert("That file is too big! Try another one");
                return;
              }
            }
            name = $("#winename").vallength();
            year = $("#year").valvintageyear();
            alcohol = $("#alcoholcontent").valnumber();
            cellar = $("#cellar").valselect();
            type = $("#winetype").valselect();
            bottles = $("#numbottles").valnumber();
            wineryName = $("#wineryname").vallength();
            price = $("#retailprice").valnumber();
            if (!name || !year || !alcohol || !cellar || !type || !bottles) {
              console.log("Error Condition");
              return;
            }
            (function(__iced_k) {
              __iced_deferrals = new iced.Deferrals(__iced_k, {
                parent: ___iced_passed_deferral1,
                filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/wine.iced"
              });
              backend.Winery.getOrCreate({
                name: wineryName
              }, __iced_deferrals.defer({
                assign_fn: (function() {
                  return function() {
                    return winery = arguments[0];
                  };
                })(),
                lineno: 54
              }));
              __iced_deferrals._fulfill();
            })(function() {
              _wine = {
                name: name,
                vintage: year,
                alcohol_content: alcohol,
                wine_type: type,
                retail_price: parseFloat(price),
                winery: winery
              };
              (function(__iced_k) {
                __iced_deferrals = new iced.Deferrals(__iced_k, {
                  parent: ___iced_passed_deferral1,
                  filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/wine.iced"
                });
                backend.Wine.getOrCreate(_wine, __iced_deferrals.defer({
                  assign_fn: (function() {
                    return function() {
                      return wine = arguments[0];
                    };
                  })(),
                  lineno: 63
                }));
                __iced_deferrals._fulfill();
              })(function() {
                _bottle = {
                  wine: "/api/v1/wine/" + wine.id + "/",
                  cellar: {
                    id: parseInt(cellar)
                  },
                  num_bottles: bottles
                };
                (function(__iced_k) {
                  __iced_deferrals = new iced.Deferrals(__iced_k, {
                    parent: ___iced_passed_deferral1,
                    filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/wine.iced"
                  });
                  backend.Bottle.update(bottle.id, _bottle, __iced_deferrals.defer({
                    assign_fn: (function() {
                      return function() {
                        return nothing = arguments[0];
                      };
                    })(),
                    lineno: 69
                  }));
                  __iced_deferrals._fulfill();
                })(function() {
                  (function(__iced_k) {
                    if ($("#imagefile").val()) {
                      (function(__iced_k) {
                        __iced_deferrals = new iced.Deferrals(__iced_k, {
                          parent: ___iced_passed_deferral1,
                          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/wine.iced"
                        });
                        backend.uploadImage(new FormData($("#upload-photo-form")[0]), bottle.id, __iced_deferrals.defer({
                          assign_fn: (function() {
                            return function() {
                              return nothing = arguments[0];
                            };
                          })(),
                          lineno: 71
                        }));
                        __iced_deferrals._fulfill();
                      })(__iced_k);
                    } else {
                      return __iced_k();
                    }
                  })(function() {
                    $("#editwine").modal("hide");
                    return renderPage();
                  });
                });
              });
            });
          });
        });
      });
    };
    return renderPage();
  });

}).call(this);
