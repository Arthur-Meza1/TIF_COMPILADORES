/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.cyberbotics.webots.controller;

public class Radar extends Device {
  private transient long swigCPtr;

  protected Radar(long cPtr, boolean cMemoryOwn) {
    super(wrapperJNI.Radar_SWIGUpcast(cPtr), cMemoryOwn);
    swigCPtr = cPtr;
  }

  protected static long getCPtr(Radar obj) {
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
        wrapperJNI.delete_Radar(swigCPtr);
      }
      swigCPtr = 0;
    }
    super.delete();
  }

  public RadarTarget[] getTargets() {
    int numberOfTargets = wrapperJNI.Radar_getNumberOfTargets(swigCPtr, this);
    RadarTarget ret[] = new RadarTarget[numberOfTargets];
    for (int i = 0; i < numberOfTargets; ++i)
      ret[i] = this.getTarget(i);
    return ret;
  }

  public Radar(String name) {
    this(wrapperJNI.new_Radar__SWIG_0(name), true);
  }

  public Radar(int tag) {
    this(wrapperJNI.new_Radar__SWIG_1(tag), true);
  }

  public void enable(int samplingPeriod) {
    wrapperJNI.Radar_enable(swigCPtr, this, samplingPeriod);
  }

  public void disable() {
    wrapperJNI.Radar_disable(swigCPtr, this);
  }

  public int getSamplingPeriod() {
    return wrapperJNI.Radar_getSamplingPeriod(swigCPtr, this);
  }

  public int getNumberOfTargets() {
    return wrapperJNI.Radar_getNumberOfTargets(swigCPtr, this);
  }

  private RadarTarget getTargetsPrivate() {
    long cPtr = wrapperJNI.Radar_getTargetsPrivate(swigCPtr, this);
    return (cPtr == 0) ? null : new RadarTarget(cPtr, false);
  }

  public double getMinRange() {
    return wrapperJNI.Radar_getMinRange(swigCPtr, this);
  }

  public double getMaxRange() {
    return wrapperJNI.Radar_getMaxRange(swigCPtr, this);
  }

  public double getHorizontalFov() {
    return wrapperJNI.Radar_getHorizontalFov(swigCPtr, this);
  }

  public double getVerticalFov() {
    return wrapperJNI.Radar_getVerticalFov(swigCPtr, this);
  }

  private RadarTarget getTarget(int index) {
    return new RadarTarget(wrapperJNI.Radar_getTarget(swigCPtr, this, index), true);
  }

}
