/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.cyberbotics.webots.controller;

public class ContactPoint {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected ContactPoint(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(ContactPoint obj) {
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
        wrapperJNI.delete_ContactPoint(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public void setPoint(double[] value) {
    wrapperJNI.ContactPoint_point_set(swigCPtr, this, value);
  }

  public double[] getPoint() {
    return wrapperJNI.ContactPoint_point_get(swigCPtr, this);
  }

  public void setNode_id(int value) {
    wrapperJNI.ContactPoint_node_id_set(swigCPtr, this, value);
  }

  public int getNode_id() {
    return wrapperJNI.ContactPoint_node_id_get(swigCPtr, this);
  }

  public void setPadding(int value) {
    wrapperJNI.ContactPoint_padding_set(swigCPtr, this, value);
  }

  public int getPadding() {
    return wrapperJNI.ContactPoint_padding_get(swigCPtr, this);
  }

  public int getNodeId() {
    return wrapperJNI.ContactPoint_getNodeId(swigCPtr, this);
  }

  public ContactPoint() {
    this(wrapperJNI.new_ContactPoint(), true);
  }

}
