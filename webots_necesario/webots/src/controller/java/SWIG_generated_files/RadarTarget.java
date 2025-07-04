/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.cyberbotics.webots.controller;

public class RadarTarget {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected RadarTarget(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(RadarTarget obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  @SuppressWarnings("deprecation")
  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        wrapperJNI.delete_RadarTarget(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public void setDistance(double value) {
    wrapperJNI.RadarTarget_distance_set(swigCPtr, this, value);
  }

  public double getDistance() {
    return wrapperJNI.RadarTarget_distance_get(swigCPtr, this);
  }

  public void setReceived_power(double value) {
    wrapperJNI.RadarTarget_received_power_set(swigCPtr, this, value);
  }

  public double getReceived_power() {
    return wrapperJNI.RadarTarget_received_power_get(swigCPtr, this);
  }

  public void setSpeed(double value) {
    wrapperJNI.RadarTarget_speed_set(swigCPtr, this, value);
  }

  public double getSpeed() {
    return wrapperJNI.RadarTarget_speed_get(swigCPtr, this);
  }

  public void setAzimuth(double value) {
    wrapperJNI.RadarTarget_azimuth_set(swigCPtr, this, value);
  }

  public double getAzimuth() {
    return wrapperJNI.RadarTarget_azimuth_get(swigCPtr, this);
  }

  public double getReceivedPower() {
    return wrapperJNI.RadarTarget_getReceivedPower(swigCPtr, this);
  }

  public RadarTarget() {
    this(wrapperJNI.new_RadarTarget(), true);
  }

}
