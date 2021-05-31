/*
 * 自定义级联插件
 * creat by may 2019/5/9
 */
(function ($) {
    $.fn.extend({
        "validation": function (options) {
            $v_t = $(this);
            var validationresult = true;
            var Vrules = function (t, Vtype, text, value) {
                validationresult = true;
                if (t.hasClass("required")) { //判定是否为空
                    var tip;
                    if (!value) {
                        tip = layer.tips(text.replace(/\s*/g, "") + '不能为空', t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "TelPhone") {
                    var rule = /^[1][0-9]{10}$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {
                        tip = layer.tips("请输入11位手机号码", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "Email") {
                    var rule = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {
                        tip = layer.tips("请输入正确的邮箱号", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "QQ") {
                    var rule = /^\d{5,12}$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {
                        tip = layer.tips("请输入正确的QQ号", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "Idcard") {
                    var rule = /^(\d){15}|(\d{17}(\d|X))$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {
                        tip = layer.tips("请输入正确的16-18位身份证号码", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "Idcard2") {
                    var rule = /(^\d{14}|^\d{17})[\dXx]$|^[A-Z][0-9]{9}$|^[A-Z][0-9]{6}\([0-9A]\)$|^[157][0-9]{6}\([0-9]\)$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {
                        tip = layer.tips("请输入正确的证件号码", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "ZipCode") {
                    var rule = /^\d{6}$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {
                        tip = layer.tips("请输入正确的邮箱号码", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "BankCard") {
                    var rule = /^\d{16,19}$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {

                        tip = layer.tips("请输入正确的银行卡号", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "Age") {
                    var rule = /^(?:[0-9][0-9]?|1[01][0-9]|120)$/;//年龄是1-120之间有效
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {

                        tip = layer.tips("请输入正确的年龄", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                if (Vtype == "Temper" && value) {
                    var rule = /^[3-4][0-9](\.[0-9])?$/;
                    var flag = rule.test(value);
                    var tip;
                    if (!flag) {
                        tip = layer.tips("请输入正确的温度", t, {
                            tips: [1, '#2E8CFF'],
                            time: 1000
                        });
                        t.val("");
                        return false;
                    } else {
                        layer.close(tip);
                    }
                }
                var newresult = options.Newrule(t, Vtype, text, value);
                if (!newresult) {
                    validationresult = false;
                }
                return validationresult
            }

            var blurflag = true;
            var submitflag;
            $v_t.find(".input-style.validate:visible").blur(function () { //失去焦点时验证              
                var t = $(this);
                var Vtype = $(this).attr("Vtype");
                var text = $(this).parent().prev(".th_left").text().replace("：", "").replace(":", "").replace("*", "");
                var value = $(this).val().trim();
                if (t.hasClass("laydate")) {//日期调用插件，不做失去焦点验证
                    blurflag = true;
                } else {
                    blurflag = Vrules(t, Vtype, text, value);
                }

            })

            num = 0
            $(".save_form").unbind().click(function () {

                if (blurflag) {//blur优先级，高于提交
                    //blurflag = true;

                    var submitvalidate = function () {
                        $v_t.find(".validate:visible").each(function (e) {//提交时验证
                            submitflag = true;
                            var t = $(this);
                            var Vtype = $(this).attr("Vtype");
                            var not_focus = false; //判断是否是focus
                            if ($(this).hasClass("input-style")) {//input框

                                var text = $(this).parent().prev(".th_left").text().replace("：", "").replace(":", "").replace("*", "");
                                var value = $(this).val().trim();

                            } else if ($(this).hasClass("select-style")) {//下拉菜单

                                var text = $(this).parents(".dropdown").prev(".th_left").text().replace("：", "").replace(":", "").replace("*", "");
                                var value = $(this).val();

                            } else if ($(this).hasClass("checkbox_list")) {//checkbox

                                var text = $(this).parent().prev(".th_left").text().replace("：", "").replace(":", "").replace("*", "");
                                if ($(this).find("input:checked").length > 0) {
                                    var value = "OK";
                                } else {
                                    var value = null;
                                }
                                not_focus = true;
                            } else if ($(this).hasClass("radio_list")) {//radio_list
                                var text = $(this).prev(".th_left").text().replace("：", "").replace(":", "").replace("*", "");
                                if ($(this).find("input:checked").length != 0) {
                                    var value = $(this).find("input:checked").val();
                                } else {
                                    var value = null;
                                }
                                not_focus = true;
                            }

                            if ($(this).attr("readonly") == "readonly" || $(this).attr("disabled") == "disabled") {
                                submitflag = true;
                            }
                            else {
                                submitflag = Vrules(t, Vtype, text, value);
                            }



                            if (!submitflag) {
                                $(this).focus();

                                if (not_focus) {//当判定focus
                                    $(this).find("input").focus();
                                }
                                return false;
                            }
                        })
                        return submitflag;
                    }
                    var returnflag = submitvalidate();

                    if (returnflag) {//执行回调事件
                        options.callback();
                    }
                }
                blurflag = true;
            })
        }
    });


})(window.jQuery);