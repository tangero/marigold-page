---
slug: "lan"
url: "/mobilnisite/slovnik/lan/"
type: "slovnik"
title: "LAN – Local Area Network"
date: 2026-01-01
abbr: "LAN"
fullName: "Local Area Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lan/"
summary: "Síť, která spojuje zařízení v omezené geografické oblasti, jako je domácnost, kancelář nebo budova. V kontextech 3GPP často odkazuje na integraci buněčných technologií (jako je 5G) s tradičními LAN pr"
---

LAN je síť spojující zařízení v omezené geografické oblasti, jako je budova, která je v rámci 3GPP integrována s buněčnými technologiemi, aby umožnila služby jako 5G LAN pro průmysl.

## Popis

V rámci specifikací 3GPP termín Local Area Network (LAN) neodkazuje na standard [IEEE](/mobilnisite/slovnik/ieee/) 802.3 Ethernet jako takový, ale spíše na koncept lokalizované komunikační sítě a, což je důležitější, na práci na integraci buněčných systémů s paradigmaty LAN. Tato integrace je klíčovým prvkem pro vertikální průmysly, jako je výroba, podnikové sféra a zdravotnictví. Standardy 3GPP, zejména od Release 16 dále, definují schopnosti 5G systémů podporovat "služby typu 5G LAN." Tyto služby umožňují 5G síti emulovat chování a charakteristiky tradiční LAN, poskytují soukromou skupinovou komunikaci, uzavřené přístupové skupiny a charakteristiky služeb podobné vrstvě 2 přes celoplošnou buněčnou infrastrukturu.

Architektonická realizace zahrnuje několik funkcí 5G core sítě. Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) jsou konfigurovány pro zpracování typů Ethernet Packet Data Unit (PDU) Session, které jsou zásadní pro přenos LAN provozu. Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) poskytuje politiky pro členství ve skupině LAN a kvalitu služeb. Klíčovým konceptem je 5G Virtual Network ([5GVN](/mobilnisite/slovnik/5gvn/)), která představuje logickou skupinu LAN. User Equipment (UE) patřící do stejné skupiny 5GVN mohou mezi sebou komunikovat přímo (prostřednictvím přepínání v UPF) nebo přes datovou síť, přičemž 5G systém spravuje členství ve skupině, její objevování a bezpečnostní izolaci od ostatních skupin.

Jak to funguje: UE naváže Ethernet PDU Session k názvu datové sítě ([DNN](/mobilnisite/slovnik/dnn/)) asociovanému se specifickou službou 5G LAN. Síť autentizuje UE a určí jeho autorizovaná členství ve skupině 5GVN. UPF funguje jako virtuální můstek nebo přepínač pro skupinu. Když UE odešle Ethernetový rámec, UPF jej může na základě cílových [MAC](/mobilnisite/slovnik/mac/) adres přeposlat ostatním UE ve stejné 5GVN s využitím svých bridging schopností, nebo jej přes rozhraní N6 směrovat do externí LAN. To poskytuje bezproblémovou konektivitu vrstvy 2 přes širokou oblast. Aspekty správy, včetně vytváření skupin, správy členství a parametrů služby, jsou zpracovávány systémy pro správu sítě ([NMS](/mobilnisite/slovnik/nms/)) a Network Exposure Function (NEF), která tyto schopnosti může zpřístupnit podnikovým aplikacím. To mění 5G systém z pouhé přístupové sítě na programovatelnou, celoplošnou LAN strukturu.

## K čemu slouží

Motivace pro standardizaci integrace LAN v 3GPP vychází z potřeby podporovat kritické aplikace Průmyslu 4.0 a podnikové aplikace, které tradičně spoléhají na kabelové Ethernet LAN nebo průmyslové bezdrátové LAN (jako Wi-Fi). Tyto aplikace vyžadují deterministickou komunikaci, ultra spolehlivou nízkou latenci, přísnou bezpečnostní izolaci a jednoduchou peer-to-peer konektivitu v rámci uzavřené skupiny – vlastnosti, které klasické služby mobilního širokopásmového přístupu nebyly navrženy poskytovat. Předchozí generace buněčných sítí nabízely přístup k internetu, ale postrádaly nativní podporu pro služby vrstvy 2 a soukromou skupinovou komunikaci, což nutilo podniky používat složité nadstavby jako VPN.

Práce 3GPP, zejména služba typu 5G LAN zavedená v Release 16, tyto nedostatky řeší tím, že činí 5G životaschopnou náhradou nebo doplňkem kabelových LAN v průmyslových prostředích. Řeší problémy mobility, pokrytí a kabelového nepořádku v továrnách, přičemž nabízí lepší spolehlivost a kontrolu ve srovnání s Wi-Fi. Vytvoření této schopnosti bylo hnací silou silné poptávky trhu z vertikálních průmyslů po jediné, sjednocené bezdrátové technologii, která by mohla podporovat jak celoplošnou mobilitu, tak lokalizovanou, kritickou komunikaci mezi stroji.

Navíc tato standardizace umožňuje síťovým operátorům nabízet podnikům nové modely "Síť jako služba". Namísto správy vlastních fyzických LAN přepínačů a Wi-Fi přístupových bodů se může podnik přihlásit k službě 5G LAN od operátora, který zřídí bezpečnou, izolovanou virtuální síť pokrývající více lokalit. To poskytuje provozní jednoduchost, škálovatelnost a integrovanou bezpečnost, což pozicuje 5G jako skutečně konvergovanou síťovou platformu pro všechny komunikační potřeby.

## Klíčové vlastnosti

- Podpora typu Ethernet PDU Session pro nativní přenos provozu vrstvy 2
- Skupiny 5G Virtual Network (5GVN) pro uzavřená, izolovaná komunikační společenství
- Komunikace UE-UE v rámci skupiny zprostředkovaná UPF fungující jako můstek
- Funkce správy skupin včetně objevování členů, procedur připojení/opuštění a řízení přístupu
- Integrace s rámcem 5G QoS pro podporu deterministické latence a spolehlivosti pro LAN provoz
- Zpřístupnění schopností správy služby LAN přes NEF pro podnikovou automatizaci

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.141** (Rel-19) — Presence Service Requirements
- **TS 22.821** (Rel-16) — 5G LAN-type Services Requirements
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.161** (Rel-12) — 3GPP-WLAN Interworking Requirements
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.252** (Rel-12) — 3GPP WLAN Interworking Charging
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [LAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/lan/)
