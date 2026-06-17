---
slug: "inipui"
url: "/mobilnisite/slovnik/inipui/"
type: "slovnik"
title: "INIPUI – IMS Network-Independent Public User Identity"
date: 2025-01-01
abbr: "INIPUI"
fullName: "IMS Network-Independent Public User Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/inipui/"
summary: "INIPUI je veřejná identita uživatele v IP Multimedia Subsystem (IMS), která je nezávislá na podkladové přístupové síti. Umožňuje konzistentní identifikaci uživatelů napříč různými typy sítí, jako je L"
---

INIPUI je veřejná identita uživatele v IMS, která je nezávislá na přístupové síti, a umožňuje konzistentní identifikaci uživatele a bezproblémové multimediální služby napříč různými typy sítí, jako je LTE nebo Wi-Fi.

## Popis

IMS Network-Independent Public User Identity (INIPUI) je typ veřejné identity uživatele definované ve specifikacích 3GPP, zejména v 22.228 a 22.894, pro použití v rámci IP Multimedia Subsystem (IMS). Slouží jako jedinečný identifikátor uživatele, který je oddělen od konkrétních přístupových sítí, jako je 5G NR, LTE nebo ne-3GPP přístup jako Wi-Fi. Na rozdíl od identit závislých na síti, které jsou vázány na konkrétní technologii, zůstává INIPUI konstantní bez ohledu na to, jak se uživatel připojí, což usnadňuje konzistentní poskytování služeb v heterogenním prostředí. Z architektonického hlediska je uložena v jádru IMS, konkrétně v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo ekvivalentních databázích, a používá se v signalizačních protokolech IMS, jako je SIP, pro navazování a správu relací. Když uživatel zahájí multimediální relaci, je INIPUI zahrnuta do zpráv SIP pro správné směrování požadavků a uplatňování servisních politik. Mezi klíčové součásti zapojené do procesu patří Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), která identitu přijímá, a Serving-CSCF (S-CSCF), která ji zpracovává pro autentizaci a spouštění služeb. INIPUI spolupracuje s privátními identitami uživatele a dalšími identifikátory, aby umožnila funkce jako jednotné přihlašování (single sign-on) a roaming. Její nezávislost na síti je klíčová pro konvergenční scénáře, umožňující operátorům nabízet jednotné služby přes více typů přístupu bez fragmentace identity. To podporuje pokročilé aplikace IMS, jako je Voice over LTE (VoLTE) nebo Rich Communication Services (RCS), tím, že zajišťuje spolehlivou identifikaci a účtování uživatelů bez ohledu na jejich způsob přístupu.

## K čemu slouží

INIPUI byla zavedena, aby řešila problém konzistentní identifikace uživatelů v IMS napříč různorodými přístupovými sítěmi, což se stalo stále důležitějším s rozšířením multi-přístupové konektivity. Před její definicí byly veřejné identity uživatelů v IMS často vázány na konkrétní typy sítí, což komplikovalo poskytování služeb, když uživatelé přepínali například mezi mobilní sítí a Wi-Fi. To mohlo vést k výpadkům služeb, nekonzistentnímu účtování nebo selhání předávání relací. INIPUI tyto problémy řeší tím, že poskytuje identitu nezávislou na síti, která zůstává stabilní, a umožňuje tak bezproblémovou mobilitu a kontinuitu služeb. Její vytvoření ve verzi 11 (Release 11) bylo motivováno růstem služeb založených na IMS, jako je VoLTE, a potřebou konvergence mezi pevnými a mobilními sítěmi. Oddělením identity od přístupu podporuje strategie operátorů pro jednotné komunikace, snižuje složitost funkcí jádra IMS a zlepšuje uživatelský zážitek tím, že umožňuje použití jediné identity pro všechny multimediální interakce. Tento vývoj odráží posun 3GPP směrem k architekturám služeb nezávislým na přístupu, kde jsou identity a služby nezávislé na podkladovém transportu.

## Klíčové vlastnosti

- Veřejná identita uživatele pro IMS nezávislá na síti
- Oddělená od konkrétních přístupových technologií, jako je 5G nebo Wi-Fi
- Používaná v signalizaci SIP pro navazování a směrování relací
- Uložená v HSS pro autentizaci a správu servisního profilu
- Podporuje bezproblémovou mobilitu napříč heterogenními sítěmi
- Umožňuje konzistentní poskytování služeb a účtování v IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.894** (Rel-11) — IMS Network-Independent Public User Identities Study

---

📖 **Anglický originál a plná specifikace:** [INIPUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/inipui/)
