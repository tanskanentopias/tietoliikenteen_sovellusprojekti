
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/adc.h>
#include <hal/nrf_saadc.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/printk.h>
#include "adc.h"

#if !DT_NODE_EXISTS(DT_PATH(zephyr_user)) || \
	!DT_NODE_HAS_PROP(DT_PATH(zephyr_user), io_channels)
#error "No suitable devicetree overlay specified"
#endif

#define DT_SPEC_AND_COMMA(node_id, prop, idx) \
	ADC_DT_SPEC_GET_BY_IDX(node_id, idx),

static const struct adc_dt_spec adc_channels[] = {
	DT_FOREACH_PROP_ELEM(DT_PATH(zephyr_user), io_channels,
			     DT_SPEC_AND_COMMA)
};





void printDebugInfo(void)
{
   printk("printing first adc_dt_spec structure contents for all channels\n");
   for(int i = 0;i<3;i++)
   {
   printk("adc_dt_spec structure, channel %d = \n",i);
   printk("Device pointer = %p\n",adc_channels[1].dev);
   printk("Channel Id = %d\n",adc_channels[i].channel_id);
   printk("Voltage reference = %d\n",adc_channels[i].vref_mv);
   printk("Resolution = %d\n",adc_channels[i].resolution);
   printk("Oversampling = %d\n",adc_channels[i].oversampling);
   printk("\n\n");
   }

}

int initializeADC(void)
{

    int err;
	
	for (size_t i = 0U; i < ARRAY_SIZE(adc_channels); i++) {
		if (!device_is_ready(adc_channels[i].dev)) {
			printk("ADC controller device not ready\n");
			return -1;
		}

		err = adc_channel_setup_dt(&adc_channels[i]);
		if (err < 0) {
			printk("Could not setup channel #%d (%d)\n", i, err);
			return -1;
		}
	}

    return 0;

}

struct Measurement readADCValue(void)
{
	int16_t buf;
    struct Measurement m;
    struct adc_sequence sequence = {
	  .buffer = &buf,

	  .buffer_size = sizeof(buf),
    };

    printk("ADC reading:\n");
	for (size_t i = 0U; i < ARRAY_SIZE(adc_channels); i++) 
    {
		int err;
        int32_t val_mv;
        // For debug use... 
		/*
        printk("- %s, channel %d: ",
		       adc_channels[i].dev->name,
		       adc_channels[i].channel_id);
        */

		(void)adc_sequence_init_dt(&adc_channels[i], &sequence);

		err = adc_read(adc_channels[i].dev, &sequence);
		if (err < 0) {
			printk("Could not read (%d)\n", err);
			continue;
		} else {
            if(i==0)
            {
                m.x = val_mv;
            }
            else if (i==1)
            {
               m.y = val_mv;
            }
            else if (i==2)
            {
                m.z = val_mv;
            }           
			//printk("%"PRId16, buf);
		}

		
		val_mv = buf;
		err = adc_raw_to_millivolts_dt(&adc_channels[i],&val_mv);
		if (err < 0) 
        {
			printk(" (value in mV not available)\n");
		} 
        else 
        {
			if(i==0)
            {
                m.x = val_mv;
            }
            else if (i==1)
            {
               m.y = val_mv;
            }
            else if (i==2)
            {
                m.z = val_mv;
            }           
            //printk(" = %"PRId32" mV\n", val_mv);
		}
	}
    return m;
}

char determine_direction() {
    // Structure to hold the measurement
    struct Measurement m = readADCValue();

    // Notify raw sensor values
    my_lbs_send_sensor_notify(m.x);
    my_lbs_send_sensor_notify(m.y);
    my_lbs_send_sensor_notify(m.z);

    // Variable to store direction
    char suunta;

    // Find the dominant axis
    float abs_x = fabs(m.x);
    float abs_y = fabs(m.y);
    float abs_z = fabs(m.z);

    if (abs_x > abs_y && abs_x > abs_z) {
        if (m.x > 0) {
            suunta = 'y'; // Positive X
            my_lbs_send_sensor_notify(1);
        } else {
            suunta = 'a'; // Negative X
            my_lbs_send_sensor_notify(-1);
        }
    } else if (abs_y > abs_x && abs_y > abs_z) {
        if (m.y > 0) {
            suunta = 'o'; // Positive Y
            my_lbs_send_sensor_notify(2);
        } else {
            suunta = 'v'; // Negative Y
            my_lbs_send_sensor_notify(-2);
        }
    } else {
        if (m.z > 0) {
            suunta = 'j'; // Positive Z
            my_lbs_send_sensor_notify(3);
        } else {
            suunta = 'i'; // Negative Z
            my_lbs_send_sensor_notify(-3);
        }
    }

    return suunta; // Return the direction as a single character
}
