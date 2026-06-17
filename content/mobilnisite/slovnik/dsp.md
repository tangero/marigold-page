---
slug: "dsp"
url: "/mobilnisite/slovnik/dsp/"
type: "slovnik"
title: "DSP – Digital Signal Processing"
date: 2025-01-01
abbr: "DSP"
fullName: "Digital Signal Processing"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dsp/"
summary: "Základní technologie pro převod reálných analogových signálů (jako hlas a rádiové vlny) na digitální data pro přenos, filtrování a analýzu. Je to jádrový matematický motor umožňující moderní bezdrátov"
---

DSP je základní technologie pro převod reálných analogových signálů na digitální data pro přenos, filtrování a analýzu a slouží jako jádrový matematický motor umožňující moderní bezdrátovou komunikaci.

## Popis

Digitální zpracování signálu (DSP) je matematické zpracování informačního signálu za účelem jeho modifikace nebo vylepšení. V kontextu systémů 3GPP je to základní technologie, která převádí analogové signály, jako je hlas nebo rádiové kmitočtové průběhy, na proud číselných digitálních hodnot. Po digitalizaci lze tyto signály s přesností a flexibilitou nedosažitelnou u čistě analogových obvodů filtrovat, komprimovat, modulovat, demodulovat a analyzovat. Proces typicky zahrnuje analogově-digitální převod ([ADC](/mobilnisite/slovnik/adc/)), aplikaci algoritmů (často implementovaných v dedikovaném hardwaru nebo softwaru) a digitálně-analogový převod ([DAC](/mobilnisite/slovnik/dac/)), pokud je vyžadován analogový výstup.

Z architektonického hlediska jsou funkce DSP zabudovány napříč uživatelským zařízením (UE) a síťovou infrastrukturou. V UE je DSP klíčové pro modem, kde zvládá úlohy jako kódování/dekódování kanálu, modulace/demodulace (např. QPSK, 256QAM) a ekvalizace. V rádiové přístupové síti (RAN) využívají základnové stanice (NodeBs, eNBs, gNBs) pokročilé DSP pro masivní [MIMO](/mobilnisite/slovnik/mimo/) formování paprsku (beamforming), prostorové multiplexování a potlačení interference. Algoritmy DSP jsou také ústřední pro hlasové kodeky (jako [AMR](/mobilnisite/slovnik/amr/) a [EVS](/mobilnisite/slovnik/evs/)) v jádru sítě, kde komprimují a paketizují řeč pro efektivní přenos.

Jeho role je všudypřítomná a kritická. DSP umožňuje efektivní využití vzácného rádiového spektra prostřednictvím sofistikovaných modulačních schémat. Zajišťuje spolehlivou komunikaci v hlučném prostředí prostřednictvím kódování pro opravu chyb. Je to umožňující technologie pro funkce jako hlas přes LTE (VoLTE) s vysokokvalitním hlasem, agregaci nosných a ultra-nízkou latenci vyžadovanou pro služby 5G Ultra-Reliable Low-Latency Communication (URLLC). Bez DSP by moderní digitální mobilní sítě definované standardy 3GPP nebyly proveditelné.

## K čemu slouží

DSP bylo vytvořeno za účelem překonání omezení analogového zpracování signálu, které bylo náchylné k šumu, zkreslení a driftu a postrádalo flexibilitu. Účelem integrace DSP do standardů 3GPP bylo umožnit přechod od analogových (1G) k digitálním (2G GSM a následným) mobilním systémům. Tento posun vyřešil základní problémy: dramaticky zlepšil kvalitu hlasu a kapacitu, umožnil šifrování pro zabezpečení a umožnil integraci datových služeb spolu s hlasem.

Historickou motivací byla potřeba spektrální efektivity a síťové kapacity s rostoucím počtem účastníků. Analogové systémy nemohly efektivně škálovat. DSP poskytlo nástroje pro implementaci komplexní digitální modulace (jako [GMSK](/mobilnisite/slovnik/gmsk/) v GSM, [OFDM](/mobilnisite/slovnik/ofdm/) v LTE/NR), která umísťuje více dat do stejné šířky pásma. Také umožnilo vývoj softwarově definovaných rádií, kde změny parametrů rozhraní vzduchu mohly být provedeny prostřednictvím softwarových aktualizací namísto změn hardwaru, což zajistilo budoucí použitelnost síťových investic a urychlilo zavádění nových funkcí napříč releasy.

## Klíčové vlastnosti

- Analogově-digitální a digitálně-analogový převod pro propojení s fyzickým světem
- Implementace modulačních a demodulačních schémat (např. OFDMA, SC-FDMA)
- Kódování kanálu a oprava chyb (např. Turbo kódy, LDPC kódy)
- Digitální filtrování a tvarování spektra pro omezení interference
- Formování paprsku (beamforming) a prostorové zpracování pro MIMO antény
- Algoritmy řečových a audio kodeků (např. AMR, EVS) pro hlasové služby

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TR 23.977** (Rel-19) — Bandwidth/Resource Savings & Speech Quality Requirements
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 45.820** (Rel-13) — CIoT for Internet of Things
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [DSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsp/)
