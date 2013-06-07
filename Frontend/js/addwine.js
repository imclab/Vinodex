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
    var cellars, html, loadWineDataIntoUI, wine, wineId, ___iced_passed_deferral, __iced_deferrals, __iced_k,
      _this = this;
    __iced_k = __iced_k_noop;
    ___iced_passed_deferral = iced.findDeferral(arguments);
    loadWineDataIntoUI = function(wine) {
      $("#winename").val(wine.name);
      $("#year").val(wine.vintage);
      $("#alcoholcontent").val(wine.alcohol_content);
      $("#winetype").val(wine.wine_type);
      $("#wineryname").val(wine.winery.name);
      $("#retailprice").val(wine.retail_price);
      $("#winenamelabel").append(wine.name);
      if (JSON.parse(wine.raw_data)) {
        return JSONParser(JSON.parse(wine.raw_data));
      } else {
        return $(".json").remove();
      }
    };
    $("#valaddwine").click(function(event) {
      var alcohol, bottle, bottles, cellar, name, newbottle, nothing, price, type, wine, wineObj, winery, wineryObj, year, ___iced_passed_deferral1, __iced_deferrals, __iced_k,
        _this = this;
      __iced_k = __iced_k_noop;
      ___iced_passed_deferral1 = iced.findDeferral(arguments);
      $("#addwine").valreset();
      event.preventDefault();
      if ($("#imagefile").val() && window.FileReader) {
        if ($("#imagefile")[0].files[0].size / (1024 * 1024) > 10) {
          alert("That file is too big! Try another one");
          return;
        }
      }
      name = $("#winename").vallength();
      year = $("#year").valvintageyear();
      alcohol = $("#alcoholcontent").vallength();
      cellar = $("#cellar").valselect();
      type = $("#winetype").valselect();
      bottles = $("#numbottles").vallength();
      winery = $("#wineryname").val();
      price = $("#retailprice").val();
      if (!name || !year || !alcohol || !cellar || !type || !bottles) {
        console.log("Error Condition");
        return;
      }
      wine = {
        name: name,
        vintage: year,
        alcohol_content: alcohol,
        wine_type: type,
        retail_price: (parseFloat(price)) || 0
      };
      (function(__iced_k) {
        if (winery) {
          (function(__iced_k) {
            __iced_deferrals = new iced.Deferrals(__iced_k, {
              parent: ___iced_passed_deferral1,
              filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/addwine.iced"
            });
            backend.Winery.getOrCreate({
              name: winery
            }, __iced_deferrals.defer({
              assign_fn: (function() {
                return function() {
                  return wineryObj = arguments[0];
                };
              })(),
              lineno: 50
            }));
            __iced_deferrals._fulfill();
          })(function() {
            return __iced_k(wine.winery = {
              id: wineryObj.id
            });
          });
        } else {
          return __iced_k();
        }
      })(function() {
        (function(__iced_k) {
          __iced_deferrals = new iced.Deferrals(__iced_k, {
            parent: ___iced_passed_deferral1,
            filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/addwine.iced"
          });
          backend.Wine.getOrCreate(wine, __iced_deferrals.defer({
            assign_fn: (function() {
              return function() {
                return wineObj = arguments[0];
              };
            })(),
            lineno: 55
          }));
          __iced_deferrals._fulfill();
        })(function() {
          bottle = {
            wine: {
              id: wineObj.id
            },
            cellar: {
              id: parseInt(cellar)
            },
            num_bottles: bottles
          };
          (function(__iced_k) {
            __iced_deferrals = new iced.Deferrals(__iced_k, {
              parent: ___iced_passed_deferral1,
              filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/addwine.iced"
            });
            backend.Bottle.create(bottle, __iced_deferrals.defer({
              assign_fn: (function() {
                return function() {
                  return newbottle = arguments[0];
                };
              })(),
              lineno: 63
            }));
            __iced_deferrals._fulfill();
          })(function() {
            (function(__iced_k) {
              if ($("#imagefile").val()) {
                (function(__iced_k) {
                  __iced_deferrals = new iced.Deferrals(__iced_k, {
                    parent: ___iced_passed_deferral1,
                    filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/addwine.iced"
                  });
                  backend.uploadImage(new FormData($("#upload-photo-form")[0]), newbottle.id, __iced_deferrals.defer({
                    assign_fn: (function() {
                      return function() {
                        return nothing = arguments[0];
                      };
                    })(),
                    lineno: 67
                  }));
                  __iced_deferrals._fulfill();
                })(__iced_k);
              } else {
                return __iced_k();
              }
            })(function() {
              return window.location = "/collection.html";
            });
          });
        });
      });
    });
    (function(__iced_k) {
      __iced_deferrals = new iced.Deferrals(__iced_k, {
        parent: ___iced_passed_deferral,
        filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/addwine.iced"
      });
      window.backend.Cellar.get({
        owner: window.backend.userId
      }, __iced_deferrals.defer({
        assign_fn: (function() {
          return function() {
            return cellars = arguments[0];
          };
        })(),
        lineno: 72
      }));
      __iced_deferrals._fulfill();
    })(function() {
      (function(__iced_k) {
        __iced_deferrals = new iced.Deferrals(__iced_k, {
          parent: ___iced_passed_deferral,
          filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/addwine.iced"
        });
        frontend.renderTemplate("addwine_cellars", {
          cellars: cellars
        }, __iced_deferrals.defer({
          assign_fn: (function() {
            return function() {
              return html = arguments[0];
            };
          })(),
          lineno: 73
        }));
        __iced_deferrals._fulfill();
      })(function() {
        $("#cellar").html(html);
        wineId = parseInt(window.location.hash.substr(1));
        if (wineId) {
          (function(__iced_k) {
            __iced_deferrals = new iced.Deferrals(__iced_k, {
              parent: ___iced_passed_deferral,
              filename: "/Users/zgrannan/Dropbox/cse110/Frontend/coffee/addwine.iced"
            });
            backend.Wine.getById(wineId, __iced_deferrals.defer({
              assign_fn: (function() {
                return function() {
                  return wine = arguments[0];
                };
              })(),
              lineno: 78
            }));
            __iced_deferrals._fulfill();
          })(function() {
            return __iced_k(loadWineDataIntoUI(wine));
          });
        } else {
          $("#winename").val(window.location.hash.substr(1));
          return __iced_k($(".json").remove());
        }
      });
    });
  });

}).call(this);
