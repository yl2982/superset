import React from 'react';
import PropTypes from 'prop-types';
import echarts from 'echarts';


class Funnel extends React.PureComponent {
    constructor(props) {
        super(props);
        this.ref = React.createRef();
    }

    componentDidMount() {
        const myChart = echarts.init(this.ref.current);
        const json = this.props.data;
        myChart.setOption(this.getOption(json));
    }

    getOption = (data = []) => {
        data.map(a => a.name = a.name.toString());
        const legendData = data.map(a => a.name);
        return {
            // title: {
            //     text: '漏斗图',
            // },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c}%"
            },
            toolbox: {
                feature: {
                    dataView: {readOnly: false},
                    restore: {},
                    saveAsImage: {}
                }
            },
            legend: {
                data: legendData
            },

            series: [
                {
                    name: '漏斗图',
                    type: 'funnel',
                    left: '10%',
                    top: 60,
                    //x2: 80,
                    bottom: 60,
                    width: '80%',
                    // height: {totalHeight} - y - y2,
                    min: 0,
                    max: 100,
                    minSize: '0%',
                    maxSize: '100%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                        show: true,
                        position: 'inside'
                    },
                    labelLine: {
                        length: 10,
                        lineStyle: {
                            width: 1,
                            type: 'solid'
                        }
                    },
                    itemStyle: {
                        borderColor: '#fff',
                        borderWidth: 1
                    },
                    emphasis: {
                        label: {
                            fontSize: 20
                        }
                    },
                    data: data
                }
            ]
        };
    }

    render() {
        const {height, width} = this.props;
        return (
            <div ref={this.ref} style={{width, height}}></div>
        );
    }
}

Funnel.defaultProps = {
    data: [],
    width: 100,
    height: 100,
};

Funnel.propTypes = {
    data: PropTypes.arrayOf(PropTypes.any),
    width: PropTypes.number,
    height: PropTypes.number,
};

export default Funnel;
