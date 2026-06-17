---
slug: "gtp-c"
url: "/mobilnisite/slovnik/gtp-c/"
type: "slovnik"
title: "GTP-C – GPRS Tunnelling Protocol for Control Plane"
date: 2026-01-01
abbr: "GTP-C"
fullName: "GPRS Tunnelling Protocol for Control Plane"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gtp-c/"
summary: "Řídicí rovinná komponenta sady protokolů GTP, odpovědná za signalizační procedury, jako je zřizování, modifikace a rušení tunelů mezi uzly jádra sítě. Spravuje kontexty relací a mobility a umožňuje dy"
---

GTP-C je řídicí rovinnou komponentou sady protokolů GTP, odpovědnou za signalizační procedury, jako je zřizování a správa tunelů mezi uzly jádra sítě, za účelem umožnění dynamické správy cest uživatelské roviny.

## Popis

GTP-C je varianta protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol pro řídicí rovinu, speciálně navržená pro zpracování signalizačních zpráv mezi prvky jádra sítě pro správu relací, správu mobility a správu tunelů. Funguje nad UDP portem 2123 a používá se v sítích od 3G do 5G, ačkoli jeho role se s architektonickými změnami vyvíjela. V sítích 3G UMTS komunikuje GTP-C mezi Serving GPRS Support Node (SGSN) a Gateway GPRS Support Node (GGSN) za účelem správy Packet Data Protocol (PDP) kontextů. V LTE/EPC se používá mezi Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving Gateway (SGW) a Packet Data Network Gateway (PGW) pro správu EPS bearerů a zpracování událostí mobility, jako jsou handovery a aktualizace oblasti sledování. Protokol používá model požadavek-odpověď, kdy iniciující uzly odesílají zprávy jako Create Session Request a odpovídající uzly reagují odpovídajícími odpověďmi, které přenášejí parametry jako Tunnel Endpoint Identifiers (TEID), QoS profily a identifikátory účtování.

Architektonicky jsou zprávy GTP-C zapouzdřeny v hlavičkách [GTP](/mobilnisite/slovnik/gtp/), které obsahují pole verze, typ zprávy, sekvenční číslo a TEID pro tunely řídicí roviny. Klíčové procedury zahrnují správu relací (aktivace, modifikace, deaktivace), správu bearerů (zřízení a zrušení datových rádiových bearerů) a správu mobility (aktualizace koncových bodů tunelů během handoverů mezi uzly). Například během procedury počátečního připojení (attach) v LTE používá MME GTP-C k odeslání Create Session Request na SGW, který jej přepošle na PGW, což vede k zřízení výchozího EPS beareru a přiřazení TEID pro uživatelskou rovinu pro tunely [GTP-U](/mobilnisite/slovnik/gtp-u/). GTP-C také podporuje mechanismy zpracování chyb a obnovy s příčinnými kódy indikujícími úspěch nebo selhání operací.

V sítích 5G se architektura řídicí roviny posunula směrem k Service-Based Interface (SBI) využívajícímu [HTTP](/mobilnisite/slovnik/http/)/2, což snížilo závislost na GTP-C pro signalizaci v jádru sítě. GTP-C však může stále být použit v určitých scénářích pro spolupráci (interworking) nebo na starších rozhraních. Protokol zahrnuje více verzí, přičemž GTPv2-C je prominentní v LTE a novějších sítích a nabízí vylepšené funkce jako podpora více PDN připojení, lepší mobilita mezi 3GPP a non-3GPP přístupem a lepší hlášení chyb. GTP-C je klíčový pro udržení kontinuity relací a efektivní využití zdrojů, protože dynamicky spravuje cesty uživatelské roviny na základě mobility účastníka a požadavků služeb.

## K čemu slouží

GTP-C byl vyvinut, aby poskytl standardizovaný signalizační mechanismus pro správu [GTP](/mobilnisite/slovnik/gtp/) tunelů v paketově přepínaných mobilních sítích, řešící potřebu dynamické správy relací a mobility. Před jeho formalizací používaly rané implementace [GPRS](/mobilnisite/slovnik/gprs/) kombinované GTP pro řídicí i uživatelskou rovinu, což postrádalo škálovatelnost a jasné oddělení funkcí. Vytvoření GTP-C jako samostatného protokolu umožnilo optimalizované signalizační procedury, které efektivně zřizují, modifikují a ruší tunely uživatelské roviny při pohybu účastníků nebo změně služeb. Vyřešil problém koordinace více síťových prvků (např. SGSN, GGSN, [MME](/mobilnisite/slovnik/mme/), SGW) pro udržení konzistentního stavu relace a zajištění plynulých handoverů.

Motivace pro GTP-C vycházela z vývoje směrem k plně IP jádru sítě v 3GPP Release 8 se System Architecture Evolution (SAE) a LTE. Jak se sítě stávaly ploššími a více distribuovanými, byl potřeba robustní protokol řídicí roviny pro správu rostoucí složitosti správy bearerů a mobility napříč více bránami. GTP-C poskytl spolehlivý, nespojovaný (connectionless) signalizační mechanismus nad UDP, vyvažující efektivitu se schopností zpracovat četné simultánní relace. Zavedl také vylepšení oproti dřívějším verzím, jako je podpora duální adresace (IPv4 a IPv6), lepší korelace účtování a lepší spolupráce s non-3GPP přístupy jako Wi-Fi.

Historicky GTP-C řešil omezení proprietárních nebo méně flexibilních signalizačních metod tím, že nabídl jednotné rozhraní, které se mohlo vyvíjet s generacemi sítí. Zatímco 5G přešlo pro většinu funkcí jádra na rozhraní řídicí roviny založené na HTTP/2, odkaz GTP-C zůstává důležitý v sítích 4G a během migračních fází. Jeho účel sahá až k umožnění pokročilých funkcí jako diferenciace kvality služby (QoS), kde řídicí zprávy přenášejí QoS parametry pro vhodnou konfiguraci tunelů uživatelské roviny, což zajišťuje, že služby jako video streaming nebo VoIP dostávají potřebné síťové zdroje.

## Klíčové vlastnosti

- Signalizace řídicí roviny pro správu GTP tunelů (vytvoření, modifikace, smazání)
- Pro přenos používá UDP port 2123, což poskytuje efektivní, nespojovanou komunikaci
- Podporuje procedury správy relací, jako je zpracování PDP kontextů a EPS bearerů
- Umožňuje správu mobility, včetně handoveru a aktualizací oblasti sledování
- Obsahuje zpracování chyb s příčinnými kódy a mechanismy obnovy
- Přenáší parametry pro QoS, účtování a přiřazení TEID

## Související pojmy

- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements

---

📖 **Anglický originál a plná specifikace:** [GTP-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/gtp-c/)
