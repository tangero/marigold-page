---
slug: "ebsg"
url: "/mobilnisite/slovnik/ebsg/"
type: "slovnik"
title: "EBSG – Elementary Basic Service Group"
date: 2025-01-01
abbr: "EBSG"
fullName: "Elementary Basic Service Group"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ebsg/"
summary: "Koncept ze služeb s přepojováním okruhů GSM/UMTS představující skupinu příbuzných telekomunikačních služeb (jako hlas, fax, data), které sdílejí společné charakteristiky předplatného a účtování. Jedná"
---

EBSG je základní jednotka pro poskytování služeb a účtování v sítích GSM/UMTS, která představuje skupinu příbuzných služeb s přepojováním okruhů sdílejících společné charakteristiky předplatného a účtování.

## Popis

Elementary Basic Service Group (EBSG) je legacy koncept pocházející z GSM a přenesený do UMTS, definovaný v kontextu telekomunikačních služeb s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Představuje logické seskupení jedné nebo více 'základních služeb' (Basic Services). Základní služba je nejzákladnější telekomunikační schopnost nabízená účastníkovi, například telefonie (hlasové hovory), fax skupiny 3 nebo různé formy dat s přepojováním okruhů (např. asynchronní data). EBSG sdružuje tyto základní služby, které sdílejí společné atributy předplatného, zejména týkající se poskytování služeb, účtování a regulatorního zacházení.

Z architektonického hlediska jsou EBSGy definovány v profilu účastníka uloženém v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Každý EBSG má přidruženou sadu parametrů, která určuje, jak se se službami ve skupině nakládá. Mezi klíčové parametry patří stav předplatného (např. povoleno, zakázáno), charakteristiky účtování (odkaz na konkrétní tarifní plán) a indikátory použitelnosti doplňkových služeb. Když mobilní účastník zahájí hovor nebo datovou relaci, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) dotazuje HLR, aby získalo profil účastníka. MSC následně zkontroluje EBSG přidružený k požadované základní službě, aby určilo, zda je hovor povolen a jaká pravidla účtování mají být použita.

Jeho role byla ústřední pro správu služeb v sítích před érou IMS. Namísto správy desítek jednotlivých základních služeb na účastníka mohli operátoři definovat několik logických EBSG (např. 'Standardní hlas a fax', 'Prémiová data', 'Blokované služby'). Toto zjednodušilo poskytování služeb, konfiguraci fakturačních systémů a implementaci balíčků služeb. Například EBSG 'Business Subscription' mohl zahrnovat telefonii, fax a vysokorychlostní data s přepojováním okruhů, vše účtované za firemní sazbu. Koncept EBSG poskytoval vrstvu abstrakce mezi základními síťovými schopnostmi (základní služby) a komerčními produkty nabízenými zákazníkům. Ačkoli je tento koncept v moderních all-IP sítích (EPS, 5GC) z velké části zastaralý, jeho pochopení je důležité pro údržbu legacy CS záložních systémů a pro pochopení historického vývoje servisní architektury v mobilních sítích.

## K čemu slouží

EBSG byl vytvořen, aby řešil provozní složitost nabízení a správy více samostatných služeb s přepojováním okruhů v sítích GSM a UMTS. Jak se sítě vyvíjely za hranice jednoduché hlasové telefonie a zahrnovaly fax, data a videotext, potřebovali operátoři způsob, jak tyto služby sdružovat do prodejných produktů a aplikovat na každý balíček konzistentní obchodní pravidla (jako účtování a blokování). Správa každé základní služby nezávisle pro miliony účastníků by byla pro systémy poskytování služeb a fakturace nepřijatelně složitá.

Primární problém, který řešil, bylo efektivní mapování mezi technickými službami na síťové úrovni a komerčními balíčky služeb. Před koncepty jako EBSG byla servisní logika a pravidla účtování často pevně zakódována nebo rozptýlena napříč více síťovými uzly, což vedlo k nekonzistentnostem a obtížím při zavádění nových balíčků služeb. EBSG poskytl standardizovaný, na profilu účastníka založený model, kde mohly být komerční nabídky definovány jako skupiny v [HLR](/mobilnisite/slovnik/hlr/). To dalo operátorům flexibilitu: mohli vytvářet různé tarifní plány kombinací EBSG a mohli měnit povolené služby účastníka pouhou úpravou přiřazení EBSG v jeho profilu.

Historicky model EBSG představoval významný krok k nezávislosti služeb na přepojovací struktuře. Abstrahoval servisní logiku do databáze účastníků, což usnadnilo zavádění nových základních služeb bez přepracování [MSC](/mobilnisite/slovnik/msc/). Tato abstrakce později připravila cestu pro pokročilejší servisní architektury, jako je [CAMEL](/mobilnisite/slovnik/camel/) pro inteligentní sítě a nakonec IP Multimedia Subsystem (IMS). Zatímco all-IP architektury LTE a 5G přešly na jiné modely služeb (založené na QoS tocích, [APN](/mobilnisite/slovnik/apn/) a IMS profilech), EBSG zůstává základním konceptem pro pochopení legacy poskytování služeb a historického kontextu vývoje mobilních služeb.

## Klíčové vlastnosti

- Logické seskupení základních služeb s přepojováním okruhů (např. telefonie, fax, data)
- Definováno v profilu účastníka v HLR/HSS pro poskytování služeb a účtování
- Přiřazuje společnou sadu charakteristik předplatného a účtování všem službám ve skupině
- Zjednodušuje správu služeb sdružováním příbuzných schopností
- Používáno MSC k autorizaci žádostí o služby a aplikaci správného účtování
- Základní koncept pro legacy architekturu služeb a fakturaci GSM/UMTS

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.016** (Rel-19) — Subscriber Data Management Stage 2
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [EBSG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ebsg/)
