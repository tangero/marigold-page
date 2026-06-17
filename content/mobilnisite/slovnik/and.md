---
slug: "and"
url: "/mobilnisite/slovnik/and/"
type: "slovnik"
title: "AND – Boolean AND"
date: 2025-01-01
abbr: "AND"
fullName: "Boolean AND"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/and/"
summary: "AND je základní booleovská logická operace definovaná ve specifikacích 3GPP pro telekomunikační systémy. Provádí logickou konjunkci na binárních vstupech a vrací hodnotu true pouze tehdy, jsou-li všec"
---

AND je základní booleovská logická operace ve specifikacích 3GPP, která provádí logickou konjunkci a vrací hodnotu true (pravda) pouze tehdy, jsou-li všechny její binární vstupy true. Je nezbytná pro řídicí logiku a rozhodování v síťových prvcích.

## Popis

Booleovská operace AND je klíčová logická funkce implementovaná napříč různými specifikacemi 3GPP a síťovými komponentami. Jako binární operátor přijímá dva nebo více booleovských hodnot jako vstup a vytváří jednu booleovskou hodnotu na výstupu podle pravidla: výstup je true (neboli logická 1), právě když jsou všechny vstupní hodnoty true; jinak je výstup false (neboli logická 0). Tato základní operace je implementována jak na hardwarové, tak softwarové úrovni v telekomunikačních systémech.

V architekturách 3GPP se operace AND vyskytuje v mnoha kontextech, včetně stavových automatů protokolů, mechanismů řízení přístupu, vyhodnocování parametrů kvality služby (QoS) a vynucování bezpečnostních politik. Například při rozhodování, zda má být uživatelskému zařízení (UE) povolen přístup ke konkrétnímu síťovému slicu, může systém vyhodnocovat více podmínek pomocí logiky AND: zda je UE autentizováno AND zda má patřičný tarif AND zda jsou dostupné síťové prostředky. Každá podmínka musí být splněna, aby byl celkový přístud udělen.

Technická implementace operací AND se liší v závislosti na kontextu v systémech 3GPP. Na fyzické vrstvě jsou hradla AND implementována pomocí tranzistorové logiky v integrovaných obvodech, které zpracovávají řídicí signály. Na vyšších vrstvách protokolů jsou operace AND implementovány prostřednictvím softwarových algoritmů v síťových funkcích a uživatelských zařízeních. Specifikace 26.094, 26.194, 46.042 a 46.082 definují, jak se operace AND používají v konkrétních telekomunikačních kontextech, zejména v testovacích postupech a požadavcích na výkon, kde je třeba vyhodnocovat logické podmínky.

Z architektonického pohledu jsou operace AND distribuovány po celé síti, nikoli centralizovány v jedné komponentě. Prvky rádiové přístupové sítě (RAN) používají logiku AND pro rozhodování o předání hovoru, funkce jádra sítě ji používají pro vynucování politik a uživatelská zařízení ji využívají pro přechody mezi stavy protokolů. Jednoduchost této operace zastírá její klíčový význam – tvoří stavební kámen pro složitější logické výrazy a rozhodovací stromy, které řídí chování sítě, přidělování prostředků a poskytování služeb v systémech 3GPP.

## K čemu slouží

Booleovská operace AND existuje jako základní logický konstrukt nezbytný pro implementaci podmíněné logiky a rozhodovacích procesů v telekomunikačních systémech. Ačkoli se může zdát základní, řeší esenciální potřebu současného vyhodnocování více podmínek v síťových operacích. Bez takových logických operací by nebylo možné efektivně implementovat komplexní podmíněná chování potřebná pro správu sítě, provádění protokolů a poskytování služeb.

Historicky digitální logické operace, jako je AND, předcházejí standardům 3GPP a mají původ v raných počítačích a návrhu digitálních obvodů. Jejich formální začlenění do specifikací 3GPP však zajišťuje standardizovanou implementaci napříč různými síťovými zařízeními od různých dodavatelů. Tato standardizace předchází problémům s interoperabilitou, které by mohly nastat, pokud by každý dodavatel implementoval podmíněnou logiku odlišně. Operace AND řeší problém vyhodnocování složených podmínek předvídatelným a standardizovaným způsobem v celém telekomunikačním ekosystému.

Motivací pro explicitní definici operací AND ve specifikacích 3GPP je potřeba jednoznačných technických požadavků. Telekomunikační systémy musí činit miliony rozhodnutí za sekundu na základě více kritérií – zda povolit předání hovoru, zda vyhovět žádosti o službu, zda použít určité QoS zacházení. Standardizací způsobu, jakým jsou tyto složené podmínky vyhodnocovány pomocí logiky AND, zajišťuje 3GPP konzistentní chování napříč sítěmi po celém světě, což je klíčové pro globální roaming, interoperabilitu a předvídatelnou kvalitu služeb.

## Klíčové vlastnosti

- Provádí logickou konjunkci na booleovských vstupech.
- Vrací hodnotu true pouze tehdy, jsou-li všechny vstupy true.
- Základní stavební kámen pro komplexní logické výrazy.
- Implementována na hardwarové i softwarové vrstvě.
- Používána pro podmíněné rozhodování v celé síti.
- Standardizována napříč specifikacemi 3GPP pro konzistenci.

## Definující specifikace

- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TS 26.194** (Rel-19) — Voice Activity Detector for AMR-WB DTX
- **TS 46.042** (Rel-19) — GSM Half-Rate Voice Activity Detector Specification
- **TS 46.082** (Rel-19) — GSM Enhanced Full Rate Voice Activity Detector

---

📖 **Anglický originál a plná specifikace:** [AND na 3GPP Explorer](https://3gpp-explorer.com/glossary/and/)
