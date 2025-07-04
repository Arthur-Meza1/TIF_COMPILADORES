/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.cyberbotics.webots.controller;

public class Skin extends Device {
  private transient long swigCPtr;

  protected Skin(long cPtr, boolean cMemoryOwn) {
    super(wrapperJNI.Skin_SWIGUpcast(cPtr), cMemoryOwn);
    swigCPtr = cPtr;
  }

  protected static long getCPtr(Skin obj) {
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
        wrapperJNI.delete_Skin(swigCPtr);
      }
      swigCPtr = 0;
    }
    super.delete();
  }

  public Skin(String name) {
    this(wrapperJNI.new_Skin__SWIG_0(name), true);
  }

  public Skin(int tag) {
    this(wrapperJNI.new_Skin__SWIG_1(tag), true);
  }

  public void setBoneOrientation(int index, double[] orientation, boolean absolute) {
    wrapperJNI.Skin_setBoneOrientation(swigCPtr, this, index, orientation, absolute);
  }

  public void setBonePosition(int index, double[] position, boolean absolute) {
    wrapperJNI.Skin_setBonePosition(swigCPtr, this, index, position, absolute);
  }

  public int getBoneCount() {
    return wrapperJNI.Skin_getBoneCount(swigCPtr, this);
  }

  public String getBoneName(int index) {
    return wrapperJNI.Skin_getBoneName(swigCPtr, this, index);
  }

  public double[] getBoneOrientation(int index, boolean absolute) {
    return wrapperJNI.Skin_getBoneOrientation(swigCPtr, this, index, absolute);
  }

  public double[] getBonePosition(int index, boolean absolute) {
    return wrapperJNI.Skin_getBonePosition(swigCPtr, this, index, absolute);
  }

}
