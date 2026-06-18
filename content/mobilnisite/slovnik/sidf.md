---
slug: "sidf"
url: "/mobilnisite/slovnik/sidf/"
type: "slovnik"
title: "SIDF – Subscription Identifier De-concealing Function"
date: 2026-01-01
abbr: "SIDF"
fullName: "Subscription Identifier De-concealing Function"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sidf/"
summary: "Bezpečnostní funkce v jádru 5G sítě, která získává trvalý identifikátor účastníka (SUPI) z jeho utajené verze (SUCI). Je to kritická součást funkce autentizačního serveru (AUSF), která umožňuje bezpeč"
---

SIDF je funkce v rámci funkce autentizačního serveru 5G sítě (AUSF), která zajišťuje získání trvalého identifikátoru účastníka (SUPI) z jeho utajené podoby (SUCI) za účelem bezpečné autentizace.

## Popis

Funkce pro odtajnění identifikátoru účastníka (SIDF) je specializovaná bezpečnostní entita zavedená v architektuře 5G systému (5GS) jako součást funkce autentizačního serveru ([AUSF](/mobilnisite/slovnik/ausf/)). Jejím hlavním technickým úkolem je provést operaci odtajnění na utajeném identifikátoru účastníka ([SUCI](/mobilnisite/slovnik/suci/)), který uživatelské zařízení (UE) zasílá během počáteční registrace v síti. SUCI je identifikátor chránící soukromí, který vytvoří UE zašifrováním trvalého identifikátoru účastníka ([SUPI](/mobilnisite/slovnik/supi/)) pomocí veřejného klíče domovské sítě. Když servisní síť (např. navštívený operátor) obdrží SUCI, přepošle jej do AUSF domovské sítě. AUSF následně vyvolá svou interní komponentu SIDF.

SIDF provede kryptografický proces odtajnění. Používá soukromý klíč domovské sítě, který odpovídá veřejnému klíči zřízenému v univerzálním [SIM](/mobilnisite/slovnik/sim/) modulu účastníka ([USIM](/mobilnisite/slovnik/usim/)) v UE, k dešifrování SUCI. Tento proces odhalí SUPI v čitelné podobě (typicky [IMSI](/mobilnisite/slovnik/imsi/) nebo síťově specifický identifikátor). SIDF je jedinou síťovou funkcí v architektuře 5G, které je dovoleno držet potřebný soukromý klíč a provádět tuto operaci, čímž se centralizuje kritická bezpečnostní funkce. Po úspěšném odtajnění AUSF použije získaný SUPI k vyhledání odpovídajících autentizačních údajů ve funkci jednotné správy dat ([UDM](/mobilnisite/slovnik/udm/)) a pokračuje v hlavní proceduře autentizace a dohody o klíčích ([AKA](/mobilnisite/slovnik/aka/)).

Z architektonického hlediska SIDF není samostatná síťová funkce (NF), ale logická funkce integrovaná v rámci AUSF. Tento návrh konsoliduje citlivý klíčový materiál a omezuje jeho vystavení. Rozhraní mezi SIDF a zbytkem AUSF je interní. Činnost SIDF je spouštěna prostřednictvím servisní operace Nausf_UEAuthentication. Její úspěšné provedení je předpokladem pro všechny následné kroky autentizace. Tím, že SIDF zajišťuje, aby SUPI nebyl nikdy přenášen v čitelné podobě přes rádiovou přístupovou síť, je klíčovým prvkem vylepšené ochrany soukromí účastníka v 5G, která chrání před odposlouchávacími zařízeními pro IMSI a útoky na sledování polohy, které byly možné v předchozích generacích. Její role je čistě pro rozlišení identifikátoru; neúčastní se následného odvozování klíčů ani navazování relace.

## K čemu slouží

SIDF byla vytvořena, aby vyřešila významnou bezpečnostní slabinu v oblasti soukromí, která byla vlastní předchozím generacím mobilních sítí (2G, 3G, 4G): přenos trvalého identifikátoru účastníka (IMSI) v čitelné podobě přes rádiové rozhraní. To umožňovalo pasivním odposlouchávačům s ne drahým vybavením získávat IMSI, sledovat polohu uživatelů a profilovat jejich pohyb. Koncepční princip 5G 'ochrany soukromí identifikátoru účastníka' vyžadoval řešení, kde trvalý identifikátor není nikdy vystaven mimo zabezpečený prostor domovské sítě. SIDF je technickým prostředníkem tohoto principu, který řeší problém, jak může síť uživatele autentizovat, aniž by zpočátku věděla, kdo uživatel je.

Historický kontext představuje vývoj od 4G EPS-AKA, kde mohl být IMSI za určitých podmínek (např. při počátečním připojení) odesílán v čitelné podobě, k povinnému použití SUCI v 5G pro počáteční registraci. SIDF provádí nezbytnou 'klíčovou' operaci, která umožňuje legitimní domovské síti – a pouze domovské síti – zjistit skutečnou identitu uživatele. Tím se řeší omezení předchozích přístupů, kde byla ochrana soukromí často volitelným doplňkem nebo se spoléhala na dočasné identifikátory (GUTI/TMSI), které mohly být stále donuceny přejít zpět na IMSI.

Její vytvoření bylo motivováno přísnými regulačními požadavky na ochranu soukromí uživatelů (např. GDPR) a potřebou průmyslu obnovit důvěru uživatelů v mobilní sítě. Centralizací odtajnění v jediné, vysoce chráněné funkci (SIDF v rámci AUSF) minimalizuje architektura 5G prostor pro možné útoky na kompromitaci přihlašovacích údajů a vytváří robustní základ pro ochranu identity, který je nedílnou součástí počátečního přístupového postupu sítě.

## Klíčové vlastnosti

- Kryptograficky odtajňuje SUCI za účelem získání SUPI pomocí soukromého klíče domovské sítě
- Je logickou funkcí striktně zabudovanou uvnitř funkce autentizačního serveru (AUSF)
- Centralizuje a chrání kritický soukromý klíč potřebný pro dešifrování identifikátoru
- Umožňuje autentizaci účastníka bez vystavení trvalého identifikátoru na rádiovém spoji
- Spouštěna prostřednictvím servisního rozhraní Nausf_UEAuthentication
- Základní prostředník pro povinnou funkci ochrany soukromí identifikátoru účastníka v 5G

## Související pojmy

- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.514** (Rel-20) — 5G Security Assurance for UDM

---

📖 **Anglický originál a plná specifikace:** [SIDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sidf/)
