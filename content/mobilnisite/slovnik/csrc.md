---
slug: "csrc"
url: "/mobilnisite/slovnik/csrc/"
type: "slovnik"
title: "CSRC – Contributing Source"
date: 2025-01-01
abbr: "CSRC"
fullName: "Contributing Source"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csrc/"
summary: "CSRC je rozhraní 3GPP definované mezi Serving Gateway (S-GW) a Packet Data Network Gateway (P-GW) v Evolved Packet Core (EPC). Přenáší uživatelskou provozní rovinu a signalizaci řídicí roviny pro rozh"
---

CSRC je rozhraní 3GPP mezi Serving Gateway a Packet Data Network Gateway, které přenáší uživatelskou provozní rovinu a signalizaci řídicí roviny pro rozhraní S5/S8 založená na GTP v Evolved Packet Core.

## Popis

Contributing Source (CSRC) je klíčový referenční bod v architektuře 3GPP Evolved Packet Core (EPC), formálně definovaný v technické specifikaci 29.414. Představuje logické rozhraní a přidruženou zásobník protokolů mezi Serving Gateway (S-GW) a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)), když jsou tyto síťové funkce nasazeny odděleně. Rozhraní CSRP je fyzická realizace založená na tomto referenčním bodu CSRC. Rozhraní podporuje jak rozhraní S5 (používané, když jsou S-GW a P-GW ve stejné PLMN pro neroucí scénáře nebo domácí směrovaný provoz), tak rozhraní S8 (používané pro roamingové scénáře, kde je S-GW ve visited PLMN a P-GW v home PLMN).

Architektonicky rozhraní CSRC využívá jako svůj základní protokol [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)). Funguje nad transportní vrstvou UDP/IP. Pro řídicí rovinu používá GTP verze 2 (GTPv2-C), definované v 3GPP TS 29.274, které zvládá procedury správy relací, jako jsou Create Session, Modify Bearer, Delete Session a Bearer Resource Command. Tyto procedury jsou nezbytné pro vytváření, modifikaci a rušení GTP tunelů (přenosových kanálů), které přenášejí uživatelská data. Pro uživatelskou provozní rovinu používá GTP verze 1 (GTPv1-U), definované v 3GPP TS 29.281, které zapouzdřují a tunelují skutečné pakety uživatelských dat (IP pakety) mezi S-GW a P-GW. Každý přenosový kanál je na obou koncích asociován s jedinečným Tunnel Endpoint Identifier (TEID).

Fungování rozhraní CSRC je klíčové pro mobilitu UE a kontinuitu relace. Když se UE připojí k síti, [MME](/mobilnisite/slovnik/mme/) vybere S-GW a P-GW. MME poté spustí vytvoření výchozího přenosového kanálu odesláním Create Session Request na S-GW, který jej přepošle na P-GW přes rozhraní CSRC. Tím se vytvoří první GTP tunel. Při předávání spojení (např. na bázi S1 nebo inter-RAT) může S-GW zůstat kotvou, zatímco se mění základnová stanice, což vyžaduje procedury modifikace přenosového kanálu přes CSRC pro aktualizaci downlink cesty. P-GW funguje jako IP kotvící bod, poskytuje přidělování IP adresy UE a vynucování politik, zatímco S-GW zvládá kotvení lokální mobility a zákonné odposlechy.

Klíčové komponenty zapojené do rozhraní CSRC zahrnují protokolové entity [GTP-C](/mobilnisite/slovnik/gtp-c/) a [GTP-U](/mobilnisite/slovnik/gtp-u/) uvnitř S-GW a P-GW, podkladovou IP transportní síť (která může využívat různé třídy QoS pro řídicí a uživatelskou rovinu) a rozhraní založená na Diameter (Gx, Gy), která P-GW používá pro interakci s Policy and Charging Rules Function (PCRF) a Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) k aplikaci politik určených během signalizace CSRC. Návrh rozhraní umožňuje, aby S-GW a P-GW byly kolidovány (v takovém případě je rozhraní S5 interní) nebo odděleny v různých geografických lokalitách, což umožňuje škálovatelná a flexibilní nasazení sítě, jako jsou centralizované fondy P-GW a distribuované S-GW.

## K čemu slouží

Rozhraní CSRC bylo vytvořeno, aby splnilo základní architektonický požadavek 3GPP System Architecture Evolution (SAE) a Evolved Packet Core (EPC) zavedených s LTE ve Release 8. Předchozí architektury paketového jádra 3GPP, jako [GPRS](/mobilnisite/slovnik/gprs/), měly monolitičtější uzly bran (GGSN). Koncepce EPC vyžadovala jasné oddělení mezi funkcí kotvení mobility (S-GW) a funkcí externí IP konektivity (P-GW). Toto oddělení si vyžádalo standardizované, robustní a škálovatelné rozhraní pro usnadnění komunikace mezi těmito nyní oddělenými síťovými funkcemi.

Primární problém, který CSRC řeší, je umožnění flexibilních a efektivních modelů nasazení sítě. Poskytnutím standardizovaného rozhraní umožňuje mobilním operátorům nasazovat S-GW a P-GW nezávisle. Operátoři mohou umístit S-GW blíže k okraji rádiové sítě pro optimalizaci latence uživatelské roviny a výkonu předávání spojení, zatímco centralizují P-GW v méně lokalitách pro zjednodušení vynucování politik, účtování a propojení s externími paketovými datovými sítěmi (jako internet nebo IMS). Toto oddělení je klíčové pro efektivní podporu jak roamingových, tak neroucích scénářů, protože rozhraní S8 (konkrétní aplikace CSRC pro roaming) umožňuje S-GW navštívené sítě bezproblémově se připojit k P-GW domovské sítě.

Dále CSRC prostřednictvím použití GTP poskytuje osvědčený tunelovací mechanismus pro správu přenosových kanálů. Řeší problém udržování kontinuity IP relace pro mobilní uživatele při jejich pohybu. GTP tunely vytvořené přes CSRC skrývají mobilitu uživatele před externí IP sítí, takže se UE z pohledu IP směrování jeví jako stacionární. Tento návrh řeší omezení dřívějších přístupů mobilního IP integrací správy mobility přímo do protokolu jádra sítě, což nabízí lepší škálovatelnost a integraci se stávajícími systémy ověřování a účtování 3GPP. Podpora více dedikovaných přenosových kanálů na výchozí kanál rozhraním také umožňuje sofistikované zpracování QoS a účtování citlivé na služby, což byly rostoucí požadavky pro nové multimediální služby.

## Klíčové vlastnosti

- Podporuje GTPv2-C pro signalizaci řídicí roviny i GTPv1-U pro tunelování uživatelské provozní roviny
- Umožňuje rozhraní S5 (neroaming/domácí směrování) a S8 (roaming) mezi S-GW a P-GW
- Poskytuje procedury správy přenosových kanálů včetně vytváření, modifikace a rušení GTP tunelů
- Umožňuje zachování IP adresy UE a kontinuitu relace během událostí mobility
- Umožňuje oddělené nasazení funkcí S-GW (okraj) a P-GW (centrum) pro síťovou flexibilitu
- Integruje se s řízením politik prostřednictvím spouštěčů na rozhraní Gx P-GW během zřizování relace

## Související pojmy

- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [CSRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/csrc/)
