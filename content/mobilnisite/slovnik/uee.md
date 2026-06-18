---
slug: "uee"
url: "/mobilnisite/slovnik/uee/"
type: "slovnik"
title: "UEE – User Equipment Emulation"
date: 2025-01-01
abbr: "UEE"
fullName: "User Equipment Emulation"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uee/"
summary: "User Equipment Emulation (UEE) je testovací a simulační metodologie zavedená ve 3GPP Release 12. Spočívá ve vytváření softwarových nebo hardwarových modelů, které napodobují chování skutečného uživate"
---

UEE je testovací metodologie využívající softwarové nebo hardwarové modely k napodobení skutečného uživatelského zařízení (User Equipment) za účelem validace síťových protokolů a funkcionalit bez nutnosti fyzických zařízení.

## Popis

User Equipment Emulation (UEE) je klíčový koncept v rámci standardů 3GPP pro účely testování a validace. Odkazuje na vytváření emulovaných instancí uživatelského zařízení (UE) – koncového zařízení jako je smartphone nebo IoT senzor – v testovacím prostředí. Tato emulace může být implementována jako software běžící na univerzálním výpočetním hardwaru nebo specializovaném testovacím zařízení. Primárním cílem je simulovat chování protokolového zásobníku, signalizační procedury a aktivity uživatelské roviny skutečného UE pro interakci se síťovými prvky, jako jsou základnové stanice (gNB/[eNB](/mobilnisite/slovnik/enb/)), funkce jádra sítě nebo testovací systémy.

Architektonicky systém UEE implementuje relevantní protokoly na straně UE definované ve specifikacích 3GPP. To zahrnuje protokoly Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) pro komunikaci s jádrem sítě (např. autentizace, správa relací) a protokoly Access Stratum ([AS](/mobilnisite/slovnik/as/)) pro rádiové rozhraní (např. simulace chování vrstev [RRC](/mobilnisite/slovnik/rrc/), [MAC](/mobilnisite/slovnik/mac/), [PHY](/mobilnisite/slovnik/phy/)). Emulaci často řídí testovací řídicí systém, který umožňuje skriptovat komplexní scénáře zahrnující více emulovaných UE pro zatěžovací testování kapacity sítě, ověření shody protokolů nebo validaci interoperability nových funkcí.

Její role v síťovém ekosystému je zásadní pro zajištění kvality. Použitím UEE mohou vývojáři testovat síťové zařízení (jako gNB) se stovkami či tisíci 'virtuálních' UE před integrací se skutečnými zařízeními. To umožňuje včasné odhalení chyb, benchmarkování výkonu pod zátěží a validaci, že síťová implementace dodržuje standardy 3GPP. Je rozsáhle používána v testování shody protokolů, zatěžovacím testování a regresním testování napříč vývojovým životním cyklem systémů 5G a budoucích generací.

## K čemu slouží

UEE byla zavedena, aby řešila významné výzvy testování komplexních a vyvíjejících se mobilních sítí. Předchozí přístupy se výrazně spoléhaly na fyzická testovací zařízení, která jsou drahá, omezená množstvím a obtížně spravovatelná pro rozsáhlé testy. Fyzická zařízení také nemusí podporovat rané nebo proprietární verze protokolů potřebné pro testování nových síťových funkcí před komerční dostupností UE. UEE tyto problémy řeší tím, že poskytuje flexibilní, softwarově definovaný testovací prostředek, který může být vytvářen ve velkém množství, konfigurován přesnými sadami parametrů a integrován do automatizovaných testovacích sad.

Vznik UEE byl motivován rostoucí komplexitou systémů 3GPP, zejména se zavedením LTE-Advanced a následným přechodem k 5G. Síťové funkce jako agregace nosných, pokročilý [MIMO](/mobilnisite/slovnik/mimo/) nebo síťové slicing vyžadují důkladné testování scénářů zahrnujících více UE s různými schopnostmi a charakteristikami provozu. UEE toto testování umožňuje v kontrolovaném laboratorním prostředí, čímž urychluje vývojové cykly a zlepšuje spolehlivost nasazovaného síťového zařízení. Je to základní metodologie odkazovaná v testovacích specifikacích jako 24.524.

## Klíčové vlastnosti

- Simuluje celý protokolový zásobník UE (NAS & AS)
- Umožňuje testování ve vysokém měřítku s tisíci virtuálních UE
- Podporuje automatizované a skriptovatelné testovací scénáře
- Validuje shodu síťových prvků se standardy 3GPP
- Umožňuje zatěžovací a výkonnostní testování za realistických podmínek
- Umožňuje testování funkcí před komerční dostupností UE

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture

---

📖 **Anglický originál a plná specifikace:** [UEE na 3GPP Explorer](https://3gpp-explorer.com/glossary/uee/)
