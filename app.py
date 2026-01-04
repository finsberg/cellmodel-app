import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import ORdmm as model

st.set_page_config(page_title="Cardiac Simulator", layout="wide")


def run_simulation(n_beats, bcl, dt, scale_params_drug):
    y_ctrl = model.init_state_values()
    y_drug = model.init_state_values()
    p_ctrl = model.init_parameter_values()
    p_drug = model.init_parameter_values(**scale_params_drug)

    t_eval = np.arange(0, bcl, dt)

    # Progress bar (simulations in browser can be slower)
    progress_bar = st.progress(0)
    status_text = st.empty()

    last_res_ctrl = None
    last_res_drug = None

    for beat in range(n_beats):
        status_text.text(f"Simulating beat {beat + 1}/{n_beats}...")

        # Control
        res_ctrl = solve_ivp(
            model.rhs,
            (0, bcl),
            y_ctrl,
            t_eval=t_eval,
            method="Radau",
            args=(p_ctrl,),
        )
        y_ctrl = res_ctrl.y[:, -1]
        last_res_ctrl = res_ctrl

        # Drug
        res_drug = solve_ivp(
            model.rhs,
            (0, bcl),
            y_drug,
            t_eval=t_eval,
            method="Radau",
            args=(p_drug,),
        )
        y_drug = res_drug.y[:, -1]
        last_res_drug = res_drug

        progress_bar.progress((beat + 1) / n_beats)

    status_text.empty()
    progress_bar.empty()

    return last_res_ctrl, last_res_drug, p_ctrl, p_drug


# --- Main App ---
def main():
    st.title("🫀 Browser-Based Cardiac Simulator")
    st.info("Running entirely in your browser using WebAssembly.")

    # Sidebar Controls
    st.sidebar.header("Settings")
    n_beats = st.sidebar.number_input("Beats", 1, 50, 10)
    bcl = st.sidebar.number_input("Cycle Length (ms)", 500.0, 2000.0, 1000.0)

    st.sidebar.subheader("Drug Scaling")
    scale_inputs = {}
    for p_name in model.parameter.keys():
        if "scale_drug" in p_name:
            default_val = float(
                model.init_parameter_values()[model.parameter_index(p_name)]
            )
            scale_inputs[p_name] = st.sidebar.slider(
                p_name, 0.0, 2.0, default_val, 0.05
            )

    # Main Plot Controls
    col1, col2 = st.columns(2)
    state_list = list(model.state.keys())
    monitor_list = list(model.monitor.keys())

    sel_state1 = col1.selectbox(
        "State", state_list, index=state_list.index("v") if "v" in state_list else 0
    )
    sel_state2 = col1.selectbox(
        "State", state_list, index=state_list.index("cai") if "cai" in state_list else 0
    )
    sel_monitor1 = col2.selectbox(
        "Monitor",
        monitor_list,
        index=monitor_list.index("IKr") if "IKr" in monitor_list else 0,
    )
    sel_monitor2 = col2.selectbox(
        "Monitor",
        monitor_list,
        index=monitor_list.index("ICaL") if "ICaL" in monitor_list else 0,
    )

    if st.button("Run Simulation", type="primary"):
        with st.spinner("Calculating... (this may take a moment in the browser)"):
            res_ctrl, res_drug, p_ctrl, p_drug = run_simulation(
                n_beats, bcl, 0.1, scale_inputs
            )

            # Prepare plotting data
            idx_state1 = model.state_index(sel_state1)
            idx_state2 = model.state_index(sel_state2)
            idx_mon1 = model.monitor_index(sel_monitor1)
            idx_mon2 = model.monitor_index(sel_monitor2)

            mon_ctrl1 = model.monitor_values(
                t=res_ctrl.t, states=res_ctrl.y, parameters=p_ctrl
            )[idx_mon1, :]
            mon_drug1 = model.monitor_values(
                t=res_drug.t, states=res_drug.y, parameters=p_drug
            )[idx_mon1, :]
            mon_ctrl2 = model.monitor_values(
                t=res_ctrl.t, states=res_ctrl.y, parameters=p_ctrl
            )[idx_mon2, :]
            mon_drug2 = model.monitor_values(
                t=res_drug.t, states=res_drug.y, parameters=p_drug
            )[idx_mon2, :]

            # Plotting
            fig, ax = plt.subplots(2, 2, sharex=True)
            ax[0, 0].plot(res_ctrl.t, res_ctrl.y[idx_state1, :], "k-", label="Control")
            ax[0, 0].plot(res_drug.t, res_drug.y[idx_state1, :], "r--", label="Drug")
            ax[0, 0].set_ylabel(sel_state1)
            ax[0, 0].legend()
            ax[1, 0].plot(res_ctrl.t, res_ctrl.y[idx_state2, :], "k-")
            ax[1, 0].plot(res_drug.t, res_drug.y[idx_state2, :], "r--")
            ax[1, 0].set_ylabel(sel_state2)
            ax[0, 1].plot(res_ctrl.t, mon_ctrl1, "k-")
            ax[0, 1].plot(res_drug.t, mon_drug1, "r--")
            ax[0, 1].set_ylabel(sel_monitor1)
            ax[1, 1].plot(res_ctrl.t, mon_ctrl2, "k-")
            ax[1, 1].plot(res_drug.t, mon_drug2, "r--")
            ax[1, 1].set_ylabel(sel_monitor2)
            ax[1, 0].set_xlabel("Time (ms)")
            ax[1, 1].set_xlabel("Time (ms)")
            fig.tight_layout()
            for axi in ax.flatten():
                axi.grid()

            st.pyplot(fig)


if __name__ == "__main__":
    main()
