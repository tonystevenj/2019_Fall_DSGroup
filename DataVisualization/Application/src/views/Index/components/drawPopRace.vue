<template>
  <div ref="race" class="wbg" style="width: 100%; height: 400px;"></div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "PopRace",
  props: {
    zipcode: {
      type: Number,
      required: true
    }
  },
  components: {},
  data() {
    return {
      chart: null
    };
  },
  mounted() {
    this.chart = echarts.init(this.$refs.race, "light");
    this.draw(this.chart, []);
    this.request();
  },
  methods: {
    request() {
      this.axios
        .get("/api/report/pop_race", {
          params: {
            zipcode: this.zipcode
          }
        })
        .then(response => {
          this.draw(this.chart, response.data);
        })
        .catch(response => {
          console.log(response);
        });
    },
    draw(chartObj, data) {
      let legendData = [];
      for (let i in data) {
        legendData.push(data[i]["name"]);
      }
      let option = {
        title: {
          text: "Race distribution",
          x: "center",
          padding: [10, 0, 0, 0]
        },
        legend: {
          x: "center",
          y: "bottom",
          padding: [0, 0, 10, 0],
          data: legendData
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {d}%"
        },
        series: [
          {
            name: "Race distribution",
            type: "pie",
            radius: "55%",
            center: ["50%", "40%"],
            data: data,
            label: {
              normal: {
                show: true,
                position: "inside",
                formatter: "{d}%"
              }
            },
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      };
      chartObj.setOption(option);
    }
  }
};
</script>