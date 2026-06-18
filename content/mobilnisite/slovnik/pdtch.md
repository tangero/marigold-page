---
slug: "pdtch"
url: "/mobilnisite/slovnik/pdtch/"
type: "slovnik"
title: "PDTCH – Packet Data Traffic Channel"
date: 2025-01-01
abbr: "PDTCH"
fullName: "Packet Data Traffic Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdtch/"
summary: "Packet Data Traffic Channel (PDTCH) je fyzický kanál v sítích GSM/GPRS/EDGE určený pro přenos paketově přepínaných uživatelských dat ve směru uplink nebo downlink. Je mobilní stanici dynamicky přidělo"
---

PDTCH je fyzický kanál v sítích GSM/GPRS/EDGE, který dynamicky přenáší paketově přepínaná uživatelská data pro mobilní stanici a umožňuje efektivní sdílení rádiových prostředků.

## Popis

Packet Data Traffic Channel (PDTCH) je základní fyzický kanál v sítích GSM, [GPRS](/mobilnisite/slovnik/gprs/) (General Packet Radio Service) a [EDGE](/mobilnisite/slovnik/edge/) (Enhanced Data rates for GSM Evolution). Používá se výhradně pro přenos paketově přepínaných uživatelských dat, jako jsou IP pakety z prohlížení webu nebo e-mailů, mezi sítí a mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)). Na rozdíl od hlasových kanálů, které jsou okruhově přepínané, je PDTCH paketově přepínaný prostředek přidělovaný na požádání a sdílený mezi více uživateli. Jedna mobilní stanice může paralelně využívat jeden nebo více PDTCH pro dosažení vyšších datových rychlostí, což je funkce známá jako multislotový provoz.

Provozně síť přiděluje prostředky PDTCH mobilní stanici, když má data k odeslání nebo příjmu. Ve směru downlink vysílá základnová stanice ([BTS](/mobilnisite/slovnik/bts/)) data na přidělených timeslotech PDTCH. Ve směru uplink používá mobilní stanice své přidělené timesloty PDTCH k odesílání dat. Přidělování řídí Packet Control Unit ([PCU](/mobilnisite/slovnik/pcu/)) na základě multislotové třídy mobilní stanice a kapacity sítě. Kanál používá modulaci Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)) v GPRS a modulaci [8-PSK](/mobilnisite/slovnik/8-psk/) v EDGE pro vyšší spektrální účinnost. Data se přenášejí v rádiových blocích, z nichž každý se skládá ze čtyř normálních GSM burstů, s robustními kódovacími schématy (CS-1 až CS-4 v GPRS; MCS-1 až MCS-9 v EDGE) vybranými na základě rádiových podmínek.

PDTCH funguje ve spojení s přidruženými řídicími kanály, jako je Packet Associated Control Channel ([PACCH](/mobilnisite/slovnik/pacch/)) pro signalizaci (např. potvrzení, přepřidělení prostředků) a Packet Timing Advance Control Channel (PTCCH) pro časové zarovnání. Jeho zavedení přeměnilo GSM z čistě hlasově orientovaného systému na systém schopný podporovat mobilní datové služby a připravilo cestu pro trvalé (always-on) připojení. Ačkoli byl nahrazen pokročilejšími kanály v sítích 3G/4G/5G, koncept PDTCH jako kanálu pro pakety přidělovaného na požádání a sdíleného ovlivnil pozdější návrhy.

## K čemu slouží

PDTCH byl vytvořen, aby do původně okruhově přepínané sítě GSM zavedl efektivní schopnosti pro paketově přepínaná data. Před GPRS používaly datové služby GSM okruhově přepínané datové kanály, které na celou dobu relace vyčlenily uživateli celý timeslot, podobně jako hovor. To bylo pro trhavý, přerušovaný datový provoz, jako je prohlížení webu, neefektivní a drahé. PDTCH tento problém vyřešil tím, že umožnil dynamické, sdílené využívání timeslotů pro datové pakety, což umožnilo statistické multiplexování a trvalé (always-on) připojení bez trvalého vyčleňování prostředků.

Jeho vývoj byl motivován rostoucí poptávkou po mobilním přístupu k internetu na konci 90. let 20. století. PDTCH jako součást GPRS umožnil operátorům sítí GSM nabízet nové služby, jako bylo prohlížení WAP, e-mail a později základní přístup k webu. Odstranil omezení předchozích přístupů tím, že poskytoval vyšší spektrální účinnost pro data, nižší dobu navazování spojení a účtování podle objemu namísto času. EDGE dále vylepšil PDTCH pomocí modulace vyššího řádu, aby zvýšil datové rychlosti v rámci stávajícího kmitočtového pásma GSM, a prodloužil tak životnost sítí 2G pro datové služby.

## Klíčové vlastnosti

- Přenáší paketově přepínaná uživatelská data v sítích GSM/GPRS/EDGE
- Dynamicky přidělován na požádání a sdílen mezi uživateli
- Podporuje multislotový provoz (více PDTCH na uživatele)
- Používá modulaci GMSK (GPRS) nebo 8-PSK (EDGE)
- Využívá více kódovacích schémat pro adaptaci spojení
- Přenáší data v rádiových blocích přes čtyři GSM bursty

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B

---

📖 **Anglický originál a plná specifikace:** [PDTCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdtch/)
