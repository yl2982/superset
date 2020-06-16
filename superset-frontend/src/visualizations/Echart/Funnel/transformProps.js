export default function transformProps(chartProps) {
    const {width, height, queryData} = chartProps;
    console.log(chartProps);
    return {
        data: queryData.data,
        width,
        height,
    };
}
