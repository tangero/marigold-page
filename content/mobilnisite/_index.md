---
title: "Mobilni site UMTS, 3G, 4G, LTE, 5G a 6G"
url: /mobilnisite/
---

## Jak fungují mobilní sítě? 

Stručný a poměrně pochopitelný úvod do toho, jak mobilní sítě fungují. Pro všechny zájemce ♥️

| Parametr | 2G | 3G | 4G | 5G | 6G |
|----------|----|----|----|----|----|
| Maximální přenosová rychlost | 384 kbit/s | 42 Mbit/s | 1 Gbit/s | 20 Gbit/s | 1 Tbit/s |
| Typické používané služby | Hlasové hovory, SMS | Mobilní internet, videohovory | Streamování videa, online hry | VR/AR, IoT, autonomní vozidla | Hologramy, rozšířená realita (XR), autonomní systémy, vzdálené operace, propojené povrchy |
| Typická hustota uživatelů na km² | 100 | 1 000 | 10 000 | 1 000 000 | 10 000 000 |
| Rok počátku rozvoje | 1991 | 2002 | 2012 | 2020 | 2030 |

## Videotutoriály pro úplné začátečníky
- [Proč jsou buňkové sítě zrovna buňkové?](https://www.youtube.com/watch?v=pz5OVB5PXA0)
- [Co je to multiplexování?](https://www.youtube.com/watch?v=FESczYohAfE)

### Sítě 2G - GSM
- jak byla [vybrána technologie GSM standardu](/item/o-vlivu-liberality-akademickeho-vzdelavani-na-ekonomicky-vynos-z-novych-odvetvi-na-prikladu-vzniku-standardu-gsm/)

### Mobilní sítě UMTS / 3G
- 3G standardem nebylo původně jen UMTS, bylo jich více, většina z nich se ale přestala používat, nebo byla do UMTS proměněného v 4G/5G "vcucnuta". Jak to [bylo se standardy 3G původně?](/item/3g-standardy-neni-jen-umts/)
- pokračujme [architekturou sítí 3G](/item/blaznuv-turbouvod-do-umts-jak-vypada-sit/), od toho se všech odvíjí
- pokračujme tím, jak to, že 3G sítě jsou o tolik kapacitnější, než 2G sítě: [Kapacita, CDMA a pár Shannonových kouzel](/item/turbouvod-do-umts-kapacita-cdma-a-par-shannonovych-kouzel)
- [IMS aneb IP Multimedia Subsystem](/item/turbouvod-do-umts-ims-aneb-ip-multimedia-subsystem/) - jak na data a multimédia v sítích 3G
- co jsou [rychlé datové přenosy v 3G pomocí HSDPA](/item/podpora-hsdpa-v-umts-release-5) - a popis toho, [jak HSDPA funguje](/item/high-speed-downlink-packet-access-hsdpa)

### Obecně k mobilním sítím
- ⏱️ Jak měl technologicky vypadat přechod k sítím LTE a 5G? Článek [Cesta k sítím 5G aneb skoro vše, co nepotřebujete vědět](/item/cesta-k-sitim-5g-aneb-skoro-vse-co-nepotrebujete-vedet/)
- ☎️ [Vývoj mobilních sítí od GSM přes 3G až k sítím 5G](/mobilnisite/mobilni-site-od-GSM-k-5G/) - shrnující přehled architektonických změn v průběhu času
- 🛜 [Signalizace v mobilních sítích](/mobilnisite/signalizace-v-mobilnich-sitich/)

### LTE
- nová architektura Jádra sítě se jmenuje [Evolved Packet Core (EPC)](/mobilnisite/epc-evolved-packet-core-lte/)
- porovnáme si [modulační technologie OFDMA versus SC-FDMA](/item/modulacni-technologie-pro-uplink-siti-4g-lte-a-wimax) (a něco si o nich řekneme)
- [LTE v nelicencovaném pásmu](/item/lte-unlicenced-o-co-jde-v-pripade-lte-v-nelicencovanem-pasmu) a jeho další rozvoj do [Licencovaného asistovaného přístupu LAA](/item/laa_release_13/)
- jak funguje [koordinované vícebodové spojení CoMP v LTE](/item/koordinovane-vicebodove-spojeni-v-lte/)
- [úzkopásmové sítě v LTE Release 8, 12 a 13](/item/varianty-lte-lpwa-jako-konkurent-sigfoxu-v-iot-v-podobe-nizkoodberovych-bezdratovych-siti/)
- přechod na [LTE Advanced](/mobilnisite/3gpp-release-10)


### 5G
- 🛜[5G NR - New Radio](/item/5G_NR_New_Radio/) - nové rádiové rozhraní
- 🗼[NG-RAN, čili rádiová přístupová síť nové generace](/item/c-ran_vran_open_ran/). Co je C-RAN, vRAN,  Open RAN
- 📡 [NTN čili Non Terrestrial Networks](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/) - připojení přes nezemské sítě
- 🕸️[5G Core](/item/5G_Core/) - jádro sítě
- ⚡️ [Integrated Access and Backhaul (IAB)](/item/integrated_access_and_backhaul_iab_5G/) čili Integrované přístupové a páteřní propojení
- 🕑 [Ultra-reliable low latency communication (URLLC)](/mobilnisite/urllc/) tedy podpora Ultra spolehlivá komunikace s nízkou latencí
- 🤖 [AI-RAN](/mobilnisite/AI-RAN/) - radiová přístupová síť optimalizovaná pro provoz AI aplikací
- 📶 [Network Slicing](/mobilnisite/network-slicing-5g/) - plátky sítě oddělené pro různé typy služeb

### Standardizace a vývoj nových funkcí v 3GPP

Zde popisuji standardizační popsuny v rámci jednotlivých Release, tedy souhrnných vydání specifikací mobilních sítí celosvětového standardu UMTS, později pojmenovaného a derivovaného na 3G, 4G, 5G a nově i 6G. Přelomové Release jsou vyznačené tučně. Začneme ale obecnějšími tématy:

📻 Jak je to s [novými frekvencemi pro 5G a 6G sítě](/item/nova-frekvenci-pasma-5g-6g/)? \
⏱️ Budoucnost frekvenčního multiplexu: [Alternativy k OFDMA jako NOMA, RSMA a SCMA](/mobilnisite/pokrocile-multiplexovani/). \
📡 [Chytré antény a jejich technologie](/item/chytre-anteny-5G-6G/)

- **Rok 1999: Release 99 jako 3G** - paketová a spínaná data PS/CS, MMS, lokalizační služby
- Rok 2001: UMTS Release 4 - první takto značená Release, zahrnuje čínské TD-SCDMA
- Rok 2002: UMTS Release 5 - HSDPA, [IMS](/item/turbouvod-do-umts-ims-aneb-ip-multimedia-subsystem/), AMR-WB
- Rok 2005: [UMTS Release 6](/item/umts-release-6) - MBMS, WLAN-UMTS, Enhanced Uplink
- Rok 2006: [UMTS Release 7](/item/vysokorychlostni-data-hspa-aneb-3gpp-release-7/) a MIMO, HSPA+, 
- **Rok 2009: [3GPP Release 8](/item/3gpp-release-8-system-architecture-evolution-sae-a-evolved-packet-core-epc-v-ramci-lte-siti) - představuje LTE/4G** jako System Architecture Evolution (SAE) a&nbsp;[Evolved Packet Core (EPC)](/mobilnisite/epc-evolved-packet-core-lte/). Podpora OFDMA
- Rok 2010: 3GPP Release 9 - [femtocelly v podobě Home eNodeB (HeNB)](/mobilnisite/hetnet), Location Services (LCS), Evolved Multimedia Broadcast/Multicast Service (eMBMS), VoLTE a Circuit Switched FallBack (CSFB)
- **Rok 2011: [3GPP Release 10 - LTE Advanced](/mobilnisite/3gpp-release-10)** a funkce CA (Carrier Aggregation), [HetNet](/mobilnisite/hetnet), [Relay Nodes (RN)](/mobilnisite/relay-node/) a [advanced MIMO](/mobilnisite/mimo).
- Rok 2013: 3GPP Release 11 - rozšiřuje funkce Rel-10 o CoMP a rozšiřuje podporu HetNet, heterogenních sítí
- Rok 2015: 3GPP Release 12 - Dual Connect, FDD-TDD CA, 245 QAM a D2D
- **Rok 2016: 3GPP Release 13 jako LTE Advanced Pro** - rozšírení pro CA a [MIMO](/mobilnisite/mimo), [nelicencovaný přístup k pásmu](/item/lte-unlicenced-o-co-jde-v-pripade-lte-v-nelicencovanem-pasmu/) vzniklé mimo standard se mění v [Licencovaný asistovaný přístup (LAA)](/item/laa_release_13/). [NB-IOT](/item/varianty-lte-lpwa-jako-konkurent-sigfoxu-v-iot-v-podobe-nizkoodberovych-bezdratovych-siti/). Gigabitový downlink.
- Rok 2017: 3GPP Release 14 - eLAA, Vehicle2Everything, Digital TV broadcast 
- **Rok 2018: 3GPP Release 15 jako 5G** - především [5G New Radio](/item/5G_NR_New_Radio/), zcela přepracovaný koncept obsahující mimo jiné škálovatelné OFDMA, [masivní MIMO a beamforming](/mobilnisite/mimo), Service Based Architecture SBA, [nové 5G Core](/item/5G_Core/) či Dual Connectivity s LTE, 
- 3GPP Release 16 - [rozšířené MIMO i beamforming](/mobilnisite/mimo) a Dynamic Spectrum Sharing DSS. [Integrované přístupové a páteřní propojení](/item/integrated_access_and_backhaul_iab_5G/), [vRAN](/item/c-ran_vran_open_ran/), [NR-U (New Radio Unlicensed)](/mobilnisite/laa-5gnr-u), podpora [IoT](/mobilnisite/redcap) a V2X
- 3GPP Release 17 - podpora 60 GHZ nelicenovaného pásma, [RedCap](/mobilnisite/redcap), [nezemských sítí NTN](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/) a sidelink relaying
- **Rok 2024: [3GPP Release 18](/item/5G_advanced_3GPP_Release-18/) jako 5G Advanced**. Technologie [eRedCap](/mobilnisite/redcap),

A co přinese budoucnost? 

![Jak bude pokračovat standardizace 5G v 3GPP](/assets/3GPP-5G-evolution.png)

- Rok 2025: [3GPP Release 19](/mobilnisite/3gpp-release-19/)
- Rok 2026: 3GPP Release 20
- Rok 2027: 3GPP Release 21 jako 6G