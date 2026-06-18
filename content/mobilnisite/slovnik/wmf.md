---
slug: "wmf"
url: "/mobilnisite/slovnik/wmf/"
type: "slovnik"
title: "WMF – WiMAX Forum"
date: 2025-01-01
abbr: "WMF"
fullName: "WiMAX Forum"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wmf/"
summary: "WiMAX Forum je průmyslové konsorcium, které podporuje a certifikuje technologii WiMAX (IEEE 802.16). Ve standardech 3GPP je na něj odkazováno v kontextu interoperabilnosti s ne-3GPP přístupovými sítěm"
---

WMF je WiMAX Forum, průmyslové konsorcium odkazované ve standardech 3GPP pro specifikaci interoperabilnosti důvěryhodných přístupových sítí WiMAX s Evolved Packet Core.

## Popis

WiMAX Forum není samo o sobě technologií 3GPP, ale externí organizací, jejíž specifikace jsou ve standardech 3GPP odkazovány za účelem umožnění interoperability se sítěmi WiMAX. WiMAX, založený na standardech [IEEE](/mobilnisite/slovnik/ieee/) 802.16, je technologií širokopásmového bezdrátového přístupu. V rámci 3GPP je role tohoto fóra klíčová pro definici, jak mohou být sítě WiMAX integrovány jako důvěryhodná ne-3GPP přístupová síť do Evolved Packet Core (EPC). Tato integrace umožňuje mobilním operátorům využívat WiMAX pro datové služby vedle jejich sítí 3GPP LTE/5G.

Architektonická integrace zahrnuje funkci sítě WiMAX jako přístupové sítě připojené k EPC prostřednictvím specifických rozhraní. Pro důvěryhodný přístup WiMAX síť zahrnuje prvky jako Access Service Network (ASN) a Connectivity Service Network (CSN), které komunikují s 3GPP Packet Data Network Gateway ([PDN](/mobilnisite/slovnik/pdn/) GW) a 3GPP serverem Authentication, Authorization, and Accounting ([AAA](/mobilnisite/slovnik/aaa/)). Specifikace WiMAX Fora zajišťují, že tyto prvky sítě WiMAX splňují protokoly a procedury požadované 3GPP pro zabezpečenou autentizaci, přidělování IP adres a vynucování politik.

Klíčové technické aspekty pokryté odkazováním na dokumenty WiMAX Fora zahrnují definici důvěryhodného přístupového bodu ([APN](/mobilnisite/slovnik/apn/)), protokoly pro vytvoření datové cesty (např. využití Proxy Mobile IP verze 6 nebo [GRE](/mobilnisite/slovnik/gre/) tunelů) a mechanismy pro autentizaci uživatele (např. založené na metodách [EAP](/mobilnisite/slovnik/eap/)). Certifikace WiMAX Fora zajišťuje, že produkty WiMAX splňují tyto požadavky na interoperabilitu, což garantuje, že zařízení nebo síťová brána od jednoho výrobce se může bezproblémově připojit k 3GPP páteřní síti od jiného výrobce. Tato standardizace je zásadní pro vytvoření jednotné uživatelské zkušenosti napříč heterogenními přístupovými technologiemi.

## K čemu slouží

Účelem odkazování na WiMAX Forum ve specifikacích 3GPP je formálně podpořit interoperabilitu mezi 3GPP mobilními páteřními sítěmi a širokopásmovými bezdrátovými sítěmi WiMAX. Historicky mobilní sítě (2G, 3G) a sítě pevného bezdrátového přístupu fungovaly odděleně. Vývoj směrem k plně IP páteřní síti (EPC) v 3GPP Rel-8 vytvořil příležitost pro sjednocení přístupu, což umožnilo operátorům nabízet služby přes jakoukoli IP přístupovou technologii, včetně WiMAX.

Toto řešilo významný obchodní a technický problém: operátoři, kteří nasadili jak sítě 3GPP, tak WiMAX, potřebovali způsob, jak nabídnout bezproblémovou mobilitu a konzistentní řízení politik napříč těmito různými typy přístupu. Bez standardizované interoperability by uživatelé měli oddělená předplatná, různé autentizační metody a nespojitou uživatelskou zkušenost. Přijetím certifikovaných specifikací WiMAX Fora zajistilo 3GPP, že WiMAX může být integrován jako 'důvěryhodný' přístup, což znamená, že páteřní síť může aplikovat stejné bezpečnostní politiky, QoS a politiky účtování jako pro přístup LTE. To umožnilo konvergované nabídky služeb a flexibilnější strategie nasazování sítí pro operátory.

## Klíčové vlastnosti

- Definuje standardy interoperability pro zařízení WiMAX
- Specifikuje protokoly pro důvěryhodný ne-3GPP přístup k 3GPP EPC
- Certifikuje produkty na shodu s požadavky 3GPP na interoperabilitu
- Podrobně popisuje postupy autentizace a zabezpečení pro přístup WiMAX
- Specifikuje tunelovací mechanismy pro vytvoření datové cesty
- Poskytuje pokyny pro řízení politik a QoS přes přístup WiMAX

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3

---

📖 **Anglický originál a plná specifikace:** [WMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/wmf/)
