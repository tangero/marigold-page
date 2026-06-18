---
slug: "smds"
url: "/mobilnisite/slovnik/smds/"
type: "slovnik"
title: "SMDS – Switched Multimegabit Data Service"
date: 2025-01-01
abbr: "SMDS"
fullName: "Switched Multimegabit Data Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smds/"
summary: "Zastaralá, nespojovaná, paketově přepínaná technologie rozlehlé datové sítě založená na IEEE 802.6 DQDB. Poskytovala vysokorychlostní přenos dat (typicky 1,5 až 45 Mbps) pro propojování LAN sítí a byl"
---

SMDS je zastaralá, nespojovaná, paketově přepínaná technologie rozlehlé sítě, která poskytovala vysokorychlostní přenos dat pro propojování LAN sítí a byla podporována v raných vydáních 3GPP.

## Popis

Switched Multimegabit Data Service (SMDS) je nespojovaná, veřejná, paketově přepínaná datová služba navržená pro rozlehlé sítě. Technicky je založena na standardu [IEEE](/mobilnisite/slovnik/ieee/) 802.6 Distributed Queue Dual Bus (DQDB) pro metropolitní sítě (MAN). SMDS funguje na vrstvě 3 (síťová vrstva) a poskytuje datagramovou službu, což znamená, že každá datová jednotka (SMDS Protocol Data Unit) je směrována nezávisle od zdroje k cíli pomocí 10místné adresy E.164, podobné telefonnímu číslu. Služba byla navržena tak, aby nabízela škálovatelnou šířku pásma od 1,5 Mbps (T1) do 45 Mbps (T3) v její severoamerické implementaci, přičemž evropské implementace používaly rychlosti E1 (2 Mbps) a E3 (34 Mbps). Podporovala funkce jako screening adres (umožňující uzavřené skupiny uživatelů) a skupinové adresování pro multicast.

V rámci architektury 3GPP, zejména v raných vydáních, byla SMDS relevantní jako jedna z externích paketových datových sítí ([PDN](/mobilnisite/slovnik/pdn/)), se kterými se mohla síť [GPRS](/mobilnisite/slovnik/gprs/) nebo UMTS propojit. Gateway GPRS Support Node (GGSN) fungoval jako rozhraní. GGSN používal Interworking Function ([IWF](/mobilnisite/slovnik/iwf/)) pro adaptaci mezi protokolem GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) používaným v jádru 3GPP a protokolem rozhraní SMDS ([SIP](/mobilnisite/slovnik/sip/)) používaným v síti SMDS. To umožňovalo mobilním účastníkům přístup k podnikovým [LAN](/mobilnisite/slovnik/lan/) sítím nebo službám nabízeným přes veřejné sítě SMDS. Přenos dat byl od konce ke konci nespojovaný; IP pakety mobilního zařízení byly zapouzdřeny v tunelech GTP směrem k GGSN, který je pak přeposílal jako rámce SMDS.

Role SMDS v 3GPP byla primárně pro zpětnou kompatibilitu a propojení během přechodu z pevných datových sítí na všudypřítomná mobilní data založená na IP. Její specifikace v dokumentech jako TS 29.061 podrobně popisují mapování protokolů a postupy propojení. Jako technologie SMDS neudržovala stav pro jednotlivé uživatelské relace, což zjednodušovalo návrh sítě, ale také to znamenalo, že postrádala vestavěné mechanismy QoS srovnatelné s pozdějšími technologiemi jako [ATM](/mobilnisite/slovnik/atm/) nebo MPLS. Její důležitost v 3GPP rychle poklesla s globálním přijetím Internet Protocol (IP) jako univerzální síťové vrstvy, díky čemuž se IP-based PDN staly standardem a odpadla potřeba složitého propojení se zastaralými MAN technologiemi.

## K čemu slouží

SMDS byla vyvinuta koncem 80. a začátkem 90. let 20. století, aby uspokojila rostoucí poptávku po vysokorychlostním, škálovatelném datovém připojení mezi geograficky rozptýlenými lokálními sítěmi (LAN). Před SMDS organizace spoléhaly na vyhrazené, point-to-point pronajaté linky (jako T1) pro propojení lokalit, což bylo drahé a nepružné. SMDS poskytovala přepínanou službu na vyžádání, která byla nákladově efektivnější pro síťové (meshed) připojení. Cílem bylo být veřejnou datovou službou ekvivalentní telefonní síti, nabízející spojení libovolného s libovolným bez nutnosti trvalých virtuálních okruhů. Její vznik byl motivován potřebou standardu pro MAN, který by mohl překlenout propast mezi rychlostmi LAN a nižšími rychlostmi služeb rozlehlých sítí (WAN) dostupných v té době.

Zařazení propojení s SMDS ve vydání 3GPP Release 4 a novějších bylo motivováno praktickou potřebou, aby sítě GPRS a UMTS poskytovaly přístup k široké škále stávajících podnikových a veřejných datových sítí. V době vzniku 3GPP byla SMDS stále nasazenou službou v některých regionech, zejména v Severní Americe a Evropě. Aby byla zajištěna široká kompatibilita a komerční životaschopnost raných 3G datových služeb, musely standardy definovat, jak se bude mobilní paketové jádro (GPRS) rozhraní s těmito zastaralými PDN. Propojení s SMDS řešilo konkrétní problém umožnění, aby se mobilní účastník jevil jako uzel ve vzdálené síti SMDS, což umožňovalo přístup k podnikovým datovým službám z doby před nástupem internetu. Tato schopnost se stala z velké části zastaralou, když se IP stalo dominantním protokolem pro veškeré datové sítě, pevné i mobilní.

## Klíčové vlastnosti

- Nespojovaná, na datagramech založená služba používající adresování E.164
- Škálovatelná šířka pásma od 1,5/2 Mbps do 34/45 Mbps
- Podpora uzavřených skupin uživatelů a skupinového adresování pro multicast
- Založena na přístupovém protokolu IEEE 802.6 DQDB pro MAN
- Definovaná propojovací funkce (Interworking Function) pro připojení k sítím 3GPP GPRS/UMTS
- V jádru sítě není udržován stav pro jednotlivá připojení

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [PDN – Packet Data Network](/mobilnisite/slovnik/pdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN

---

📖 **Anglický originál a plná specifikace:** [SMDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/smds/)
