package com.perlaca.gcs

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.repeatOnLifecycle
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.maps.android.ktx.addMarker
import com.google.maps.android.ktx.awaitMap
import com.google.maps.android.ktx.cameraMoveEvents
import kotlinx.coroutines.launch

class MapMissionFragment : Fragment() {
    private var googleMap: GoogleMap? = null

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.CREATED) {
                val mapFragment = childFragmentManager.findFragmentById(R.id.map) as? SupportMapFragment
                googleMap = mapFragment?.awaitMap()
                googleMap?.let { map ->
                    val veracruzBase = LatLng(19.3750, -96.5020)
                    map.addMarker {
                        position(veracruzBase)
                        title("Base Operativa PERLACOLABS - STR-002 H3 v3.5")
                    }
                }
            }
        }
    }
}
