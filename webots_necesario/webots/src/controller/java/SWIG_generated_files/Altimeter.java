/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.cyberbotics.webots.controller;

public class Altimeter extends Device {
  private transient long swigCPtr;

  protected Altimeter(long cPtr, boolean cMemoryOwn) {
    super(wrapperJNI.Altimeter_SWIGUpcast(cPtr), cMemoryOwn);
    swigCPtr = cPtr;
  }

  protected static long getCPtr(Altimeter obj) {
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
        wrapperJNI.delete_Altimeter(swigCPtr);
      }
      swigCPtr = 0;
    }
    super.delete();
  }

  public Altimeter(String name) {
    this(wrapperJNI.new_Altimeter__SWIG_0(name), true);
  }

  public Altimeter(int tag) {
    this(wrapperJNI.new_Altimeter__SWIG_1(tag), true);
  }

  public void enable(int samplingPeriod) {
    wrapperJNI.Altimeter_enable(swigCPtr, this, samplingPeriod);
  }

  public void disable() {
    wrapperJNI.Altimeter_disable(swigCPtr, this);
  }

  public int getSamplingPeriod() {
    return wrapperJNI.Altimeter_getSamplingPeriod(swigCPtr, this);
  }

  public double getValue() {
    return wrapperJNI.Altimeter_getValue(swigCPtr, this);
  }

}
