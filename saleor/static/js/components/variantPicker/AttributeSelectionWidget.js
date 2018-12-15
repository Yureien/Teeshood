import React, { Component, PropTypes } from 'react';
import classNames from 'classnames';

export default class AttributeSelectionWidget extends Component {

  static propTypes = {
    attribute: PropTypes.object.isRequired,
    handleChange: PropTypes.func.isRequired,
    selected: PropTypes.string
  };

  handleChange = (attrPk, valuePk) => {
    this.props.handleChange(attrPk.toString(), valuePk.toString());
  }

  render() {
      const { attribute, selected } = this.props;
	  let sizeChart;
	  if (attribute.name === "Size") {
		  sizeChart = <small><a href="" data-toggle="modal" data-target="#myModal-chart">Size Chart</a></small>
	  }
      return (
		  <div className="variant-picker product-size">
          <h5 className="sub-title">{attribute.name} {sizeChart}</h5>
          {attribute.values.map((value, i) => {
              const active = selected === value.pk.toString();
              const labelClass = classNames({
				  'active': active
              });
            return (
				<label
                className={labelClass}
                key={i}
                onClick={() => this.handleChange(attribute.pk, value.pk)}>
                <input
                defaultChecked={active}
                name={value.pk}
                type="radio"/>
                <span className={labelClass}>{value.name}</span>
				</label>
            );
        })}
        </div>
    );
  }
}
