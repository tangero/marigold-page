---
slug: "ccp"
url: "/mobilnisite/slovnik/ccp/"
type: "slovnik"
title: "CCP – Capability/Configuration Parameter"
date: 2025-01-01
abbr: "CCP"
fullName: "Capability/Configuration Parameter"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ccp/"
summary: "Standardizovaná datová struktura v kartách USIM/UICC dle 3GPP, která uchovává schopnosti a konfigurační nastavení mobilního zařízení. Umožňuje síti efektivně dotazovat a porozumět charakteristikám kon"
---

CCP je standardizovaná datová struktura v kartách USIM/UICC dle 3GPP, která uchovává schopnosti a konfigurační nastavení mobilního zařízení pro dotazování sítě, poskytování služeb a optimalizaci.

## Popis

Parametr schopností/konfigurace (CCP) je základní datový prvek definovaný ve specifikacích 3GPP pro aplikace modulu univerzálního účastnického identifikátoru ([USIM](/mobilnisite/slovnik/usim/)) a karty univerzálního integrovaného obvodu (UICC). Je uložen jako vyhrazený soubor ([EF](/mobilnisite/slovnik/ef/)_CCP) v systému souborů USIM a je strukturován dle specifikací TS 31.102. CCP není jediná hodnota, ale strukturovaný záznam obsahující více polí, z nichž každé reprezentuje konkrétní schopnost koncového zařízení nebo konfigurační nastavení. Tato pole jsou kódována pomocí konstrukcí Tag-Length-Value ([TLV](/mobilnisite/slovnik/tlv/)), což umožňuje rozšiřitelnost a začlenění nových parametrů s vývojem technologie napříč vydáními 3GPP.

Hlavní funkcí CCP je sloužit jako trvalé, síti přístupné úložiště vlastních schopností uživatelského zařízení (UE) a konfiguračních preferencí definovaných uživatelem nebo operátorem. Když se UE připojí k síti nebo během specifických procedur, může síť přečíst soubor CCP z USIM pomocí standardizovaných příkazů. To umožňuje síťové entitě (např. Mobile Management Entity - [MME](/mobilnisite/slovnik/mme/) nebo Access and Mobility Management Function - [AMF](/mobilnisite/slovnik/amf/)) získat okamžitý přehled o tom, co terminál podporuje, aniž by se spoléhala pouze na signalizaci v reálném čase nebo potenciálně neúplné informace z rádiové vrstvy UE. Data pokrývají širokou škálu aspektů, včetně podporovaných technologií rádiového přístupu (např. [GERAN](/mobilnisite/slovnik/geran/), [UTRAN](/mobilnisite/slovnik/utran/), [E-UTRAN](/mobilnisite/slovnik/e-utran/), NR), kmitočtových pásem, podporovaných funkcí pro hlasové služby (jako schopnost IMS voice over PS session), preferencí pro zpracování SMS a parametrů souvisejících s mobilitou a správou relací.

Z architektonického hlediska CCP představuje kritický rozhraní mezi vyměnitelným USIM/UICC (který je vázán na předplatné) a řídicí rovinou mobilní sítě. Jeho existence odděluje některé znalosti specifické pro terminál od volatilní paměti UE a ukládá je na nevymazatelnou, přenosnou SIM kartu. To je obzvláště důležité pro funkce závislé na předplatném nebo tam, kde operátor chce vynutit určité konfigurace. Síť zpracovává informace v CCP, aby mohla činit informovaná rozhodnutí. Může například určit, zda povolit předání spojení (handover) k určité rádiové technologii, zda zahájit IMS hlasové volání, nebo jak směrovat SMS zprávy na základě deklarovaných schopností a nastavení UE.

Během provozu je čtení CCP typicky spouštěno síťovými procedurami. Síťová strana iniciuje příkaz USIM Application Toolkit (USAT) nebo příkaz pro přístup k souboru, aby získala EF_CCP. Přístup zprostředkovává modem UE a rozhraní SIM. Získaná data jsou následně použita síťovými algoritmy pro správu rádiových prostředků, správu mobility a poskytování služeb. Role CCP se rozšířila z původně primárního kontextu GSM/UMTS v dřívějších vydáních tak, aby zahrnovala schopnosti LTE a 5G NR, což z ní činí konzistentní mechanismus pro zjišťování schopností napříč generacemi. Jeho správa zahrnuje jak výrobce UE, který nastavuje počáteční příznaky schopností, tak mobilního síťového operátora, který může aktualizovat konfigurační parametry prostřednictvím platformy Over-The-Air (OTA) a tak upravit data na USIM.

## K čemu slouží

CCP byl zaveden, aby vyřešil základní problém asymetrických informací mezi mobilní sítí a uživatelským zařízením (UE). V raných mobilních systémech měly sítě omezené prostředky, jak spolehlivě a efektivně zjistit, jaké funkce konkrétní telefon podporuje. To mohlo vést k neúspěšným pokusům o služby, suboptimální alokaci prostředků nebo zhoršenému uživatelskému zážitku. Síť se například mohla pokusit předat hovor do kmitočtového pásma, které telefon nepodporoval, což způsobilo přerušení. CCP poskytuje standardizovaný, trvalý a autoritativní zdroj těchto informací uložený na samotné SIM kartě.

Jeho vytvoření bylo motivováno potřebou inteligentnějšího síťového řízení a personalizace služeb. Díky centralizovanému záznamu schopností vázanému na identitu předplatného (IMSI) může síť přizpůsobovat své chování proaktivně. To je efektivnější než odvozování schopností ze sporadických signalizačních zpráv nebo modelů zařízení. Také umožňuje operátorům vzdáleně konfigurovat určité chování UE prostřednictvím aktualizací SIM OTA, což umožňuje zavádění nových funkcí nebo opravu konfiguračních problémů bez nutnosti aktualizace firmwaru telefonu. To dává operátorům větší kontrolu nad kvalitou služeb ve své síti.

CCP dále řeší výzvu diverzity zařízení. Když mobilní trh zaplavily tisíce různých modelů zařízení, každý s různou kombinací hardwarových a softwarových funkcí, stal se statický, standardizovaný mechanismus hlášení nezbytným pro škálovatelnou správu sítě. Umožňuje základním síťovým uzlům aplikovat konzistentní logiku bez ohledu na konkrétní typ UE, přičemž rozhodnutí jsou založena na parametrech načtených z CCP. To zjednodušuje síťovou architekturu a zlepšuje interoperabilitu mezi síťovými zařízeními od různých dodavatelů a množstvím zařízení v provozu.

## Klíčové vlastnosti

- Strukturované ukládání schopností UE v oblasti technologií rádiového přístupu (např. podpora GERAN, UTRAN, E-UTRAN, NR)
- Kóduje informace o podpoře kmitočtových pásem pro efektivní výběr sítě a předání spojení (handover)
- Obsahuje konfigurační parametry pro služby základní sítě, jako jsou SMS a hlas přes IMS
- Používá kódování TLV (Tag-Length-Value) pro flexibilitu a budoucí rozšiřitelnost
- Uložen jako vyhrazený soubor (EF_CCP) v systému souborů USIM/UICC, přístupný prostřednictvím standardizovaných příkazů
- Podporuje vzdálené aktualizace prostřednictvím SIM OTA (Over-The-Air) provizionování ze strany síťového operátora

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [EF – Elementary File](/mobilnisite/slovnik/ef/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [CCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccp/)
