"""Icon helpers for BMW CarData descriptors."""

from __future__ import annotations

from typing import Optional

# Explicit overrides for descriptors where a single icon makes sense.
_EXACT_DESCRIPTOR_ICONS: dict[str, str] = {
    "vehicle.drivetrain.electricEngine.charging.status": "mdi:ev-station",
    "vehicle.drivetrain.electricEngine.charging.level": "mdi:battery-charging-high",
    "vehicle.powertrain.electric.battery.stateOfCharge.target": "mdi:battery-charging-high",
    "vehicle.drivetrain.electricEngine.remainingElectricRange": "mdi:map-marker-distance",
    "vehicle.drivetrain.totalRemainingRange": "mdi:map-marker-distance",
    "vehicle.drivetrain.fuelSystem.remainingFuel": "mdi:gas-station",
    "vehicle.drivetrain.fuelSystem.level": "mdi:gas-station",
    "vehicle.vehicle.travelledDistance": "mdi:speedometer",
    "vehicle.vehicle.avgSpeed": "mdi:speedometer",
    "vehicle.status.conditionBasedServices": "mdi:wrench",
    "vehicle.status.checkControlMessages": "mdi:car-tire-alert",
    "vehicle.vehicle.preConditioning.activity": "mdi:fan",
    "vehicle.vehicle.preConditioning.remainingTime": "mdi:clock-outline",
    "vehicle.vehicle.preConditioning.error": "mdi:alert-circle-outline",
    "vehicle.vehicle.preConditioning.isRemoteEngineRunning": "mdi:engine",
    "vehicle.vehicle.preConditioning.isRemoteEngineStartAllowed": "mdi:engine",
    "vehicle.vehicle.avgAuxPower": "mdi:flash",
    "vehicle.channel.teleservice.status": "mdi:phone",
    "vehicle.body.chargingPort.status": "mdi:ev-plug-type2",
    "vehicle.body.chargingPort.lockedStatus": "mdi:lock",
    "vehicle.body.trunk.isOpen": "mdi:car-back",
    "vehicle.body.trunk.isLocked": "mdi:lock",
    "vehicle.cabin.hvac.preconditioning.status.remainingRunningTime": "mdi:clock-outline",
}


def icon_for_descriptor(descriptor: Optional[str]) -> Optional[str]:
    """Return a material design icon for a BMW CarData descriptor."""

    if not descriptor:
        return None

    if descriptor in _EXACT_DESCRIPTOR_ICONS:
        return _EXACT_DESCRIPTOR_ICONS[descriptor]

    lowered = descriptor.lower()

    if "remaining" in lowered and "range" in lowered:
        return "mdi:map-marker-distance"
    if "fuel" in lowered:
        return "mdi:gas-station"
    if "soc" in lowered or "stateofcharge" in lowered or lowered.endswith(".hvsoc"):
        if "charging" in lowered:
            return "mdi:battery-charging-high"
        return "mdi:car-battery"
    if "battery" in lowered and "charge" in lowered:
        return "mdi:battery-charging-high"
    if "battery" in lowered:
        return "mdi:car-battery"
    if "charging" in lowered:
        if "amp" in lowered:
            return "mdi:current-ac"
        if "volt" in lowered:
            return "mdi:current-ac"
        if "time" in lowered:
            return "mdi:clock-outline"
        if "connector" in lowered or "plug" in lowered:
            return "mdi:ev-plug-type2"
        return "mdi:ev-station"
    if "power" in lowered:
        return "mdi:flash"
    if "voltage" in lowered:
        return "mdi:flash"
    if "amp" in lowered:
        return "mdi:current-ac"
    if "pressure" in lowered:
        return "mdi:car-tire-alert"
    if "temperature" in lowered or lowered.endswith(".ect"):
        return "mdi:thermometer"
    if "tire" in lowered:
        return "mdi:car-tire-alert"
    if "hvac" in lowered or "climate" in lowered or "preconditioning" in lowered:
        return "mdi:fan"
    if "seat" in lowered:
        if "heating" in lowered:
            return "mdi:car-seat-heater"
        if "cooling" in lowered:
            return "mdi:air-conditioner"
        return "mdi:car-seat"
    if "door" in lowered or "window" in lowered:
        return "mdi:car-door"
    if "sunroof" in lowered:
        return "mdi:weather-sunny"
    if "trunk" in lowered:
        return "mdi:car-back"
    if "hood" in lowered:
        return "mdi:car"
    if "lock" in lowered:
        return "mdi:lock"
    if "engine" in lowered or "ignition" in lowered:
        return "mdi:engine"
    if "navigation" in lowered or "location" in lowered or "gps" in lowered:
        return "mdi:map-marker"
    if "service" in lowered:
        return "mdi:wrench"
    if "diagnostic" in lowered or "fault" in lowered:
        return "mdi:alert"
    if "alarm" in lowered:
        return "mdi:alarm-light"
    if "sleep" in lowered:
        return "mdi:power-sleep"
    if "time" in lowered or "timestamp" in lowered:
        return "mdi:clock-outline"
    if "speed" in lowered or "distance" in lowered or "travelled" in lowered:
        return "mdi:speedometer"
    if "phone" in lowered or "teleservice" in lowered:
        return "mdi:phone"
    if "sim" in lowered:
        return "mdi:sim"

    return None
