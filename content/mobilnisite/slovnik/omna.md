---
slug: "omna"
url: "/mobilnisite/slovnik/omna/"
type: "slovnik"
title: "OMNA – Open Mobile Naming Authority"
date: 2025-01-01
abbr: "OMNA"
fullName: "Open Mobile Naming Authority"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/omna/"
summary: "Open Mobile Naming Authority (OMNA) je registr spravovaný 3GPP pro přidělování jedinečných identifikátorů používaných v protokolech a službách mobilních sítí. Zajišťuje globální jedinečnost parametrů,"
---

OMNA je registr spravovaný 3GPP, který přiděluje jedinečné identifikátory pro protokoly a služby mobilních sítí, aby zajistil globální interoperabilitu.

## Popis

Open Mobile Naming Authority (OMNA), specifikovaná v 3GPP TS 26.346, funguje jako centrální registrační a přidělovací autorita pro různé názvy, identifikátory a kódové body používané napříč technickými specifikacemi 3GPP. Jejím hlavním úkolem je udržovat registr jedinečných hodnot, aby se předešlo kolizím a zajistila jednoznačná interpretace polí protokolů a parametrů služeb v prostředích s více dodavateli. OMNA spravuje přidělování identifikátorů pro širokou škálu entit, včetně, ale ne pouze, identifikátorů přístupového bodu služby (SAPI) používaných v komunikaci protokolových vrstev, diskriminátorů protokolů, typů zpráv a výčtových hodnot pro funkce v rámci multimediálních a dalších domén služeb.

Z architektonického hlediska OMNA není síťový prvek, ale administrativní funkce provozovaná 3GPP. Poskytuje veřejně přístupný registr (často publikovaný online), kde jsou uvedeny přidělené číselné hodnoty a jejich odpovídající definice. Když je v rámci 3GPP standardizován nový protokol, služba nebo funkce vyžadující jedinečný identifikátor, příslušná pracovní skupina podá žádost OMNA o přidělení hodnoty. Tento proces se řídí postupy 3GPP, aby byla zajištěna řízená a koordinovaná alokace. Záznamy v registru typicky obsahují hodnotu identifikátoru, krátký popis, specifikaci, která definuje jeho použití, a organizaci žadatele.

Jak to funguje, je spíše procesní než běhovou záležitostí. Ve fázi vývoje standardů návrháři protokolů identifikují potřebu jedinečného identifikátoru. Následují proces 3GPP pro získání hodnoty z registru OMNA. Jakmile je hodnota přidělena, je zakotvena do příslušné specifikace 3GPP. Výrobci zařízení a vývojáři softwaru pak implementují své produkty podle těchto specifikací s použitím hodnot přidělených OMNA. Za běhu, když síťový prvek přijme protokolovou zprávu, může prozkoumat pole obsahující identifikátory spravované OMNA (např. SAPI v rámci vrstvy 2), aby správně určil zamýšlenou službu nebo protokolovou entitu pro další zpracování. Tento mechanismus je zásadní pro vrstvou protokolovou architekturu mobilních sítí, protože umožňuje různým vrstvám a partnerským entitám komunikovat jednoznačně.

## K čemu slouží

OMNA byla vytvořena k řešení problému kolize identifikátorů a správy jmenných prostorů v rychle se vyvíjejícím a vysoce standardizovaném ekosystému 3GPP. Jak specifikace 3GPP narůstaly a zahrnovaly stovky protokolů, služeb a volitelných funkcí, stala se potřeba centralizované, neutrální autority pro alokaci jedinečných kódových bodů kritickou. Bez takové autority by různí dodavatelé nebo různé pracovní skupiny 3GPP mohli nezávisle přiřadit stejnou číselnou hodnotu různým významům, což by vedlo ke katastrofálním selháním interoperability při pokusu o komunikaci zařízení z různých zdrojů.

Její zavedení, zvláště patrné od vydání 12 v kontextu multimediálních služeb a vyvíjejících se protokolů, bylo motivováno rozšířením působnosti 3GPP za čistý rádiový přístup do oblastí bohatých multimédií, IoT a rámců pro poskytování služeb. Tyto nové domény přinesly četné nové protokoly a parametry vyžadující standardizaci. OMNA poskytuje škálovatelné a budoucím potřebám odolné řešení pro správu identifikátorů. Řeší omezení ad-hoc nebo specifikaci-specifických metod přidělování, které bylo obtížné globálně udržovat napříč celou sadou specifikací 3GPP. Tím, že poskytuje jediný zdroj pravdy pro tyto identifikátory, OMNA snižuje chyby při implementaci, zjednodušuje testování a certifikaci a v konečném důsledku zajišťuje, že „42“ v poli protokolu znamená totéž pro ruční zařízení od výrobce A, základnovou stanici od výrobce B a jádro sítě od výrobce C.

## Klíčové vlastnosti

- Centralizovaný registr pro přidělování jedinečných identifikátorů v rámci 3GPP
- Zabraňuje kolizím v jmenném prostoru mezi různými protokoly a dodavateli
- Spravuje identifikátory přístupového bodu služby (SAPI) pro komunikaci mezi vrstvami
- Přiděluje diskriminátory protokolů a typy zpráv
- Poskytuje výčtové hodnoty pro multimediální a servisní parametry
- Veřejně přístupný a řízený postupy 3GPP

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols

---

📖 **Anglický originál a plná specifikace:** [OMNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/omna/)
