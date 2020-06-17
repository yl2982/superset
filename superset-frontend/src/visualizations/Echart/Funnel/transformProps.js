export default function transformProps(chartProps) {
    const {width, height, queryData} = chartProps;
    return {
        data: queryData.data,
        width,
        height,
    };
}
