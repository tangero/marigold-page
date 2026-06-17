---
slug: "msid"
url: "/mobilnisite/slovnik/msid/"
type: "slovnik"
title: "MSID – Mobile Station Identifier"
date: 2025-01-01
abbr: "MSID"
fullName: "Mobile Station Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msid/"
summary: "MSID je obecný termín pro jakýkoli identifikátor používaný k jednoznačnému rozlišení mobilní stanice (UE) v rámci mobilní sítě. Slouží jako zastřešující koncept pro konkrétní identifikátory, jako jsou"
---

MSID je obecný zastřešující termín pro jakýkoli identifikátor, například IMSI nebo IMEI, používaný k jednoznačnému rozlišení mobilní stanice (Mobile Station) v rámci mobilní sítě.

## Popis

Mobile Station Identifier (MSID) je základní koncepce vysoké úrovně ve standardech 3GPP, která označuje jakýkoli identifikátor jednoznačně určující mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), dnes běžně známou jako uživatelské zařízení (UE), v kontextu mobilní sítě. Nejde o jediný konkrétní identifikátor s definovaným formátem, ale spíše o kategorický termín zahrnující různé jedinečné názvy nebo čísla přiřazené UE nebo jeho předplatnému. Tyto identifikátory jsou klíčové pro všechny síťové operace, včetně registrace, autentizace, správy mobility, účtování a bezpečnostních procedur.

Architektura pro MSID zasahuje do více síťových domén. Identifikátory jsou uloženy v různých síťových entitách: v samotném UE (v USIM nebo paměti zařízení), v rádiové přístupové síti (RAN), v jádře sítě (CN) a často i v externích databázích, jako je Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)). 'Jak funguje' je specifické pro každý typ MSID. Například International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) používá jádro sítě k získání autentizačních dat předplatitele z [HSS](/mobilnisite/slovnik/hss/). Dočasný identifikátor předplatitele (TMSI) přiděluje Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) za účelem zajištění důvěrnosti identity předplatitele na rádiovém rozhraní, čímž po počáteční registraci nahrazuje IMSI.

Klíčové součásti rámce MSID zahrnují trvalé identifikátory (jako IMSI a International Mobile Equipment Identity neboli [IMEI](/mobilnisite/slovnik/imei/)), dočasné identifikátory (jako TMSI, [GUTI](/mobilnisite/slovnik/guti/) a S-TMSI) a identifikátory rádiové sítě (jako C-RNTI používané pro plánování v rámci buňky). Úlohou MSID je poskytovat jednoznačnou adresaci na různých vrstvách a pro různé účely: trvalou identitu předplatitele pro správu a roaming, dočasnou identitu pro ochranu na vzdušném rozhraní, dočasnou identitu síťové vrstvy pro směrování v oblasti sledování a dočasnou identitu na úrovni buňky pro řízení rádiových prostředků. Síť mezi těmito identifikátory plynule mapuje, když se UE připojuje, pohybuje a komunikuje.

## K čemu slouží

Koncepce Mobile Station Identifier existuje k řešení základního požadavku na jedinečné pojmenování a adresování mobilního koncového bodu v rozsáhlé globální síti. Rané mobilní systémy potřebovaly způsob, jak odlišit telefon jednoho předplatitele od druhého pro směrování hovorů, účtování a základní síťový přístup. Účelem definice MSID jako obecného termínu je poskytnout jasný architektonický zástupný symbol a klasifikaci pro všechny konkrétní identifikátory, které byly vyvinuty, z nichž každý řeší konkrétní dílčí problém identifikace.

Různé MSID byly vytvořeny k řešení konkrétních omezení. Trvalý IMSI vyřešil problém globálně jedinečné identifikace předplatitele pro roaming. Časté vysílání trvalého IMSI po rádiu však představovalo bezpečnostní riziko (např. sledování, zachycení identity). Toto omezení motivovalo vytvoření dočasných identifikátorů, jako je TMSI, které poskytují důvěrnost identity. Podobně byl vytvořen IMEI k identifikaci hardwaru zařízení nezávisle na předplatném, což pomáhá řešit problémy jako blokování odcizených zařízení. Vývoj MSID odráží neustálé úsilí o vyvážení potřeb jedinečné identifikace, provozní efektivity, soukromí předplatitele a bezpečnosti napříč stále složitějšími síťovými architekturami a službami.

## Klíčové vlastnosti

- Zastřešující termín pro všechny identifikátory UE/předplatného v systémech 3GPP
- Zahrnuje trvalé identifikátory (IMSI, IMEI) a dočasné identifikátory (TMSI, GUTI)
- Nezbytný pro procedury jádra sítě, jako je autentizace, správa mobility a účtování
- Kritický pro procedury rádiové sítě, jako je paging a plánování spojení
- Zahrnuje identifikátory s různými rozsahy: globální, síťové, na úrovni oblasti sledování a na úrovni buňky
- Tvoří základ klíčových síťových funkcí včetně bezpečnosti (důvěrnost identity) a roamingu

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/msid/)
