import React from "react";
import {useParams} from "react-router-dom";
import LoggerFactory from "../../service/LoggerFactory";
import CourseInfo from "./CourseInfo";

const logger = LoggerFactory.getLogger("CourseInfoView")
export default function CourseInfoView() {
    const {id} = useParams();

    return (<CourseInfo id={id}/>);
}