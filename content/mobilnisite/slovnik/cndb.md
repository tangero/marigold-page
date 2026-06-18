---
slug: "cndb"
url: "/mobilnisite/slovnik/cndb/"
type: "slovnik"
title: "CNDB – Calling Name Database"
date: 2025-01-01
abbr: "CNDB"
fullName: "Calling Name Database"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cndb/"
summary: "Databáze jmen volajících (CNDB) je síťový prvek, který ukládá a poskytuje informace o jméně volajícího pro účastníky. Umožňuje zobrazení jména volajícího na zařízení příjemce během hlasových hovorů, č"
---

CNDB je síťový prvek, který ukládá a poskytuje informace o jméně volajícího, aby umožnil zobrazení jména volajícího na zařízení příjemce.

## Popis

Databáze jmen volajících (CNDB) je specializovaná síťová databáze definovaná ve specifikacích 3GPP, která ukládá informace o jméně účastníka přidružené k telefonním číslům ([MSISDN](/mobilnisite/slovnik/msisdn/)). Funguje jako systém dotaz-odpověď, kde síťové prvky, typicky Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), mohou vyžádat informace o jméně volajícího pro služby prezentace. Při zahájení hovoru obslužný síťový prvek dotazuje CNDB pomocí MSISDN volajícího a databáze vrátí odpovídající jméno účastníka, pokud je dostupné a autorizované k prezentaci.

Architektura CNDB následuje centralizovaný nebo distribuovaný databázový model v závislosti na implementaci operátora. Rozhraní s prvky jádra sítě využívá standardizované protokoly, primárně operace [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) přes sítě [SS7](/mobilnisite/slovnik/ss7/) (Signaling System No. 7). Databáze udržuje záznamy účastníků obsahující mapování MSISDN-jméno spolu s příznaky služby udávajícími povolení prezentace, nastavení soukromí a stav předplatného. Tyto záznamy jsou zřizovány prostřednictvím správních systémů operátora a mohou být aktualizovány dynamicky na základě požadavků účastníka nebo změn v síti.

Při provozu CNDB vykonává několik klíčových funkcí: ověřuje autorizaci dotazujících se síťových prvků, kontroluje preference soukromí účastníka, načítá informace o jménu ze své databáze, formátuje odpověď podle požadavků prezentace a zaznamenává transakce pro účely účtování a auditu. Databáze podporuje dotazy jak v rámci sítě, tak mezi sítěmi, což umožňuje prezentaci jména volajícího napříč různými sítěmi operátorů, pokud existují roamingové dohody. Požadavky na výkon zahrnují nízkou latenci odpovědí (typicky pod 500 ms), aby se zabránilo zpožděním při sestavování hovoru, a vysokou dostupnost (99,999 % doby provozuschopnosti), aby byla zajištěna spolehlivost služby.

Role CNDB přesahuje pouhé načítání jmen a zahrnuje vykonávání servisní logiky. Aplikuje obchodní pravidla, jako jsou preference formátování jmen (např. pouze křestní jméno, celé jméno), řeší speciální případy, jako jsou firemní účastníci s názvy oddělení, a spravuje scénáře přepsání, kde účastníci mohou blokovat prezentaci jména. Databáze také podporuje integraci doplňkových služeb, což umožňuje kombinovat jméno volajícího se službami, jako je Caller ID, Call Waiting a Conference Calling. Bezpečnostní funkce zahrnují autentizaci dotazujících se entit, šifrování citlivých dat a mechanismy řízení přístupu, aby se zabránilo neoprávněnému získávání jmen.

## K čemu slouží

CNDB byla vytvořena, aby řešila rostoucí poptávku po rozšířených službách volání nad rámec základní identifikace čísla. Před jejím zavedením mobilní sítě primárně zobrazovaly pouze telefonní číslo volajícího ([MSISDN](/mobilnisite/slovnik/msisdn/)), což poskytovalo omezenou identifikaci a špatný uživatelský zážitek. Účastníci měli potíže s rozpoznáním volajících pouze z čísel, zejména u kontaktů, které neměli uložené v telefonním seznamu. Toto omezení se stalo výraznějším s rostoucím rozšířením mobilních telefonů a tím, že uživatelé přijímali hovory od různých obchodních kontaktů, poskytovatelů služeb a příležitostných volajících.

Technologie řeší problém identifikace volajícího tím, že poskytuje čitelné jméno spolu s telefonním číslem. To zlepšuje uživatelský zážitek tím, že umožňuje příjemcům činit informovaná rozhodnutí o přijetí hovoru, zlepšuje dostupnost pro zrakově postižené uživatele prostřednictvím převodu textu na řeč a umožňuje profesionální komunikační scénáře, kde je třeba prezentovat organizační názvy. CNDB také řeší obavy o soukromí prostřednictvím konfigurovatelných nastavení prezentace, což dává účastníkům kontrolu nad tím, kdy se jejich jména zobrazí.

Historicky služby prezentace jména volajícího existovaly ve sítích pevných linek, ale nebyly standardizovány pro mobilní sítě. 3GPP zavedlo CNDB ve verzi Release 4, aby vytvořilo jednotný přístup napříč sítěmi GSM/UMTS, což umožnilo interoperabilitu mezi zařízeními různých dodavatelů a konzistentní poskytování služeb přes hranice operátorů. Standardizovaný databázový přístup nahradil proprietární implementace, které bránily roamingu a službám mezi operátory, a vytvořil základ pro přidané služby, které mohli operátoři monetizovat při současném zlepšování spokojenosti zákazníků.

## Klíčové vlastnosti

- Ukládání a vyhledávání mapování MSISDN na jméno
- Rozhraní protokolu MAP pro dotazy síťových prvků
- Mechanismy kontroly soukromí účastníka a prezentace
- Podpora dotazů mezi operátory pro roamingové scénáře
- Architektura s vysokou dostupností a nízkou latencí odpovědí
- Integrace s HLR/MSC pro signalizaci sestavování hovoru

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [CNDB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cndb/)
