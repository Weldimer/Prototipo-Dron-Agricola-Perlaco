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
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

/**
 * Fragmento de Estación de Control Terrestre (GCS) - STR-002 H3 v3.5
 * Utiliza Maps KTX y Corrutinas para renderizado asíncrono y control de telemetría en tiempo real.
 */
class MapMissionFragment : Fragment() {

    private var googleMap: GoogleMap? = null

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Inicialización segura del mapa mediante Corrutinas y Lifecycle
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.CREATED) {
                val mapFragment = childFragmentManager.findFragmentById(R.id.map) as? SupportMapFragment
                googleMap = mapFragment?.awaitMap()

                googleMap?.let { map ->
                    // Configuración de marcador de referencia (Ej. Zona de Operación Veracruz)
                    val veracruzBase = LatLng(19.3750, -96.5020)
                    map.addMarker {
                        position(veracruzBase)
                        title("Base Operativa PERLACOLABS - STR-002 H3 v3.5")
                    }

                    // Recopilación de eventos de movimiento de cámara mediante Flows
                    launch {
                        map.cameraMoveEvents().collect {
                            // Evento de desplazamiento o zoom en el mapa de misiones
                        }
                    }
                }
            }
        }
    }
}
