package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloWorldController {
    @RequestMapping("/")
    @ResponseBody
    public String hello() {
        return "Hello SpringBoot Version:v2";
    }
    @RequestMapping("/healthy")
    @ResponseBody
    public String healthy() {
        return "ok";
    }
}
