---
slug: "msin"
url: "/mobilnisite/slovnik/msin/"
type: "slovnik"
title: "MSIN – Mobile Station Identification Number"
date: 2025-01-01
abbr: "MSIN"
fullName: "Mobile Station Identification Number"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msin/"
summary: "MSIN je klíčová, národně významná část mezinárodního identifikátoru mobilního účastníka (IMSI). Jednoznačně identifikuje účastníka v rámci domény konkrétního mobilního operátora a je využíván operátor"
---

MSIN je národně významná část IMSI, která jednoznačně identifikuje účastníka v rámci domény konkrétního mobilního operátora.

## Popis

Mobile Station Identification Number (MSIN) je kritickou součástí mezinárodního identifikátoru mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), který je primárním trvalým identifikátorem mobilního předplatného. IMSI je strukturován jako řetězec desítkových číslic, typicky o délce 15 číslic, rozdělený na tři části: Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/), 3 číslice), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/), 2 nebo 3 číslice) a MSIN (až 10 číslic). MSIN je část přiřazená mobilním operátorem ([MNO](/mobilnisite/slovnik/mno/)) k jednoznačné identifikaci účastníka v rámci jeho sítě, jak je definováno MCC a MNC.

Z architektonického hlediska je MSIN uložen na [USIM](/mobilnisite/slovnik/usim/) kartě účastníka a slouží jako klíč používaný jádrovou sítí k vyhledání předplatitelských dat. Když se UE připojuje k síti, může prezentovat IMSI. Síť (konkrétně [MME](/mobilnisite/slovnik/mme/) v LTE/5G nebo [SGSN](/mobilnisite/slovnik/sgsn/)/[VMSC](/mobilnisite/slovnik/vmsc/) ve starších systémech) použije MCC a MNC k směrování žádosti o autentizaci do správné sítě operátora. Jakmile je požadavek v domovské síti operátora, HSS (Home Subscriber Server) nebo jeho předchůdce HLR (Home Location Register) použije celé IMSI, přičemž MSIN je primárním klíčem, k nalezení konkrétního záznamu účastníka ve své databázi. Tento záznam obsahuje autentizační údaje účastníka (Ki), servisní profil, povolené služby a další předplatitelská data.

Jeho fungování je nedílnou součástí správy účastníků. Z pohledu signalizačních protokolů rádiového rozhraní a jádra sítě je MSIN neprůhledné číslo; tyto protokoly zacházejí s IMSI jako s celkem. Pro interní administrativní a databázové systémy operátora je však MSIN jedinečným identifikátorem předplatného. Jeho úlohou je poskytnout jednoznačnou identifikaci na úrovni operátora. Používá se nejen pro vyhledávání v HSS/HLR, ale také pro generování záznamů o účtování (CDR), provizování služeb a správu životního cyklu účastníka. Hodnota MSIN je klíčová pro korelaci všech síťových událostí a využití služeb s konkrétním zákaznickým účtem.

## K čemu slouží

MSIN byl vytvořen jako součást struktury IMSI k vyřešení problému škálovatelné a jedinečné identifikace účastníků v rámci sítě jednoho operátora. Rané mobilní systémy potřebovaly způsob, jak spravovat potenciálně miliony účastníků. Jednoduché sekvenční číslo (MSIN) přiřazené z národního číselného prostoru, kombinované s kódy země a sítě (MCC/MNC), vytvořilo globálně jedinečný identifikátor (IMSI), který byl zásadní pro automatický roaming.

Účelem MSIN je poskytnout v rámci globálně jedinečné struktury IMSI jedinečný klíč definovaný operátorem. Řeší omezení pouhého kódu sítě (MNC) tím, že umožňuje operátorovi rozlišit všechny své účastníky. Jeho vytvoření bylo motivováno potřebou hierarchického adresovacího schématu: MCC směruje do země, MNC směruje k operátorovi v této zemi a MSIN konečně identifikuje účastníka u tohoto operátora. Tato struktura je efektivní pro databázová vyhledávání a směrování v mezinárodních roamingových scénářích. MSIN navíc poskytuje operátorům flexibilitu v jejich číslovacích plánech; mohou strukturovat číslice MSIN tak, aby kódovaly informace jako typ účastníka nebo region, ačkoli toto je specifické pro operátora a pro standardní síťové procedury transparentní.

## Klíčové vlastnosti

- Operátorem přiřazená část IMSI, dlouhá až 10 číslic
- Jednoznačně identifikuje účastníka v rámci konkrétního Mobile Network Code (MNC)
- Slouží jako primární klíč pro záznam účastníka v databázi HLR/HSS
- Nezbytný pro procesy jádrové sítě: autentizaci, autorizaci služeb a účtování
- Globálně jedinečný v kombinaci s MCC a MNC
- Trvale asociován s USIM a předplatným, s výjimkou přenosu čísla nebo výměny

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [MSIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/msin/)
