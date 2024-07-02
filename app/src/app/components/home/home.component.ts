import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { ReportService } from 'src/app/services/report.service';
import * as XLSX from 'xlsx';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  tables: string[] = ['Events'];
  relatedTables: string[] = ['Classifications', 'Venues', 'Attractions'];
  selectedTables: string[] = [];
  selectedMainTable!: string;
  reportData: any;
  isSubmitting: boolean = false;
  requestError: boolean = false;
  errorMessage: string = "";

  operators = {
    comparison: ["=", "!=", ">", "<", ">=", "<=", "like", "ilike"],
    logical: ["AND", "OR"],
    groupBy: ["COUNT", "SUM", "MIN", "MAX"],
    orderBy: ["ASC", "DESC"]
  }

  eventFields: any;
  venuesFields: any;
  classificationsFields: any;
  attractionsFields: any;
  modeFields: any;

  form: FormGroup;

  displayedColumns: string[] = ["Aguardando consulta para carregar a tabela..."];
  dataSource = new MatTableDataSource<any>([]);

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild('TABLE') table!: ElementRef
  @ViewChild('chartCanvas') chartCanvas!: ElementRef;

  constructor(
    private reportService: ReportService,
    private formBuilder: FormBuilder
  ) {
    this.form = this.formBuilder.group({
      selectedMainTable: [''],
      selectedRelatedTables: [[]],

      eventTableFields: [[]],
      classificationsTableFields: [[]],
      attractionsTableFields: [[]],
      eventModeTableFields: [[]],
      venuesTableFields: [[]],

      eventTableFilters: [[]],
      classificationsTableFilters: [[]],
      attractionsTableFilters: [[]],
      eventModeTableFilters: [[]],
      venuesTableFilters: [[]],

      eventOperator1: [null],
      eventOperator2: [null],
      eventOperator3: [null],
      eventValue1: [null],
      eventValue2: [null],
      eventValue3: [null],

      classificationsOperator1: [null],
      classificationsOperator2: [null],
      classificationsOperator3: [null],
      classificationsValue1: [null],
      classificationsValue2: [null],
      classificationsValue3: [null],

      venuesOperator1: [null],
      venuesOperator2: [null],
      venuesOperator3: [null],
      venuesValue1: [null],
      venuesValue2: [null],
      venuesValue3: [null],

      attractionsOperator1: [null],
      attractionsOperator2: [null],
      attractionsOperator3: [null],
      attractionsValue1: [null],
      attractionsValue2: [null],
      attractionsValue3: [null],

      eventModeOperator1: [null],
      eventModeOperator2: [null],
      eventModeOperator3: [null],
      eventModeValue1: [null],
      eventModeValue2: [null],
      eventModeValue3: [null],

      selectedAggsTable: "Events",
      aggsParam: [null],
      logicalOperator: [null],
      orderBy: [null],
      func_agregada: [null],
      isChecked: [null]
    });
  }

  ngOnInit(): void {
    this.dataSource.data = [];
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  } 

  exportAsExcel() {
    const allData = this.dataSource.data;
    const tableData: any[] = [];
  
    // Iterar pelos registros e adicionar os dados à matriz
    allData.forEach((row: any) => {
      const rowData: any[] = [];
  
      // Iterar pelas colunas e obter os valores correspondentes
      this.displayedColumns.forEach((column: string) => {
        rowData.push(row[column]);
      });
  
      // Adicionar a linha de dados à matriz
      tableData.push(rowData);
    });
  
    // Criar uma planilha do Excel a partir dos dados da tabela
    const ws: XLSX.WorkSheet = XLSX.utils.aoa_to_sheet(tableData);
    const wb: XLSX.WorkBook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
  
    // Salvar o arquivo do Excel
    XLSX.writeFile(wb, 'report.xlsx');
  }

  clearForm() {
    this.selectedTables = [];
    this.selectedMainTable = "";
    this.form.reset();
  }

  clearTable(dataSource: MatTableDataSource<any>, paginator: MatPaginator): void {
    // Limpa o dataSource definindo um novo array vazio
    dataSource.data = [];
    this.displayedColumns = ["Aguardando consulta para carregar a tabela..."];
  
    // Reseta o paginator
    if (paginator) {
      paginator.firstPage();
    }

    setTimeout(() => {
      this.requestError = false;
    }, 5000);
  }

  updateTableColumnsAndData(data: any) {
    this.dataSource.data = [];
    this.displayedColumns = ["Aguardando consulta para carregar a tabela..."];
    // this.paginator.length = data.length;

    if (data.length > 0) {
      this.dataSource.data = data;
      this.displayedColumns = Object.keys(data[0]);
      this.paginator.length = data.length;
    } else {
      this.displayedColumns = [];
    }
  }

  getTableStructure(tableName: string) {
    switch (tableName) {
      case "Events":
        this.eventFields = ['id', 'name', 'url', 'startdatesale', 'enddatesale', 'startdateevent', 'timezone', 'minprice', 'maxprice', 'promoter', 'venueid', 'classificationsid'];
        break;

      case "Venues":
        this.venuesFields = ['id', 'name', 'url', 'postalCode', 'timezone', 'city', 'state', 'country', 'addres'];
        break;

      case "Classifications":
        this.classificationsFields = ['id', 'name', 'segmentid', 'segmentName'];
        break;

      case "Attractions":
        this.attractionsFields = ['id', 'name', 'url', 'classificationsid'];
        break;
    }
  }

  onMainTableSelectionChange(): void {
    const selectedMainTable = this.form.controls['selectedMainTable'].value;

    this.selectedMainTable = selectedMainTable;
    this.form.controls['selectedRelatedTables'].setValue([]);
    this.selectedTables = [selectedMainTable];

    this.getTableStructure(selectedMainTable);
  }

  onRelatedTablesSelectionChange(): void {
    const selectedRelatedTables = this.form.controls['selectedRelatedTables'].value;

    // Remover as tabelas que não estão mais selecionadas
    this.selectedTables = this.selectedTables.filter(table => table === 'Events' || selectedRelatedTables.includes(table));

    // Adicionar as novas tabelas selecionadas
    selectedRelatedTables.forEach((element: string) => {
      if (element !== 'Events' && !this.selectedTables.includes(element)) {
        this.selectedTables.push(element);
      }
    });

    this.selectedTables.forEach(table => {
      this.getTableStructure(table);
    });
  }

  submitForm(form: any) {
    this.isSubmitting = true;

    let data: any = {};
    let request: any = {
      select: {},
      join: [],
      where: {},
      operators: {},
      values: {},
      condition: form.controls.logicalOperator.value,
      order_by: null,
      func_agregada: null,
      group_by: form.get('isChecked')?.value
    };

    (Object.keys(form.controls) as (keyof typeof form.controls)[]).forEach((key, index) => {
      if (key !== "selectedRelatedTables") {
        if (Array.isArray(form.controls[key].value) && form.controls[key].value.length > 0) {
          data[key] = form.controls[key].value;
        }
      }
    });

    data.selectedTables = this.selectedTables;
    
    this.selectedTables.forEach(table => {
      if (table === "Events") {
        request.select.events = data.eventTableFields;
        request.join.push("events");
        request.where.events = data.eventTableFilters;
        request.operators.events = [form.controls.eventOperator1.value, form.controls.eventOperator2.value, form.controls.eventOperator3.value];
        request.values.events = [form.controls.eventValue1.value, form.controls.eventValue2.value, form.controls.eventValue3.value];
       }
      request = this.formatData(request, form);
    })


    console.log(request);
    this.reportService.queryData(request).subscribe({
      next: (response) => {
        this.isSubmitting = false;
        this.updateTableColumnsAndData(response);
        console.log(response);
      },
      error: (err) => {
        this.clearTable(this.dataSource, this.paginator);
        this.isSubmitting = false;
        this.requestError = true;
        this.errorMessage = "Não foi possível realizar a consulta, verifique os parâmetros e tente novamente";
      }
    });    
  }

  // Agrupa a informação separando pelo nome da tabela em questão
  addRequestInfo(request: any, form: any, table: any) {
    const tableName = table;

    if (!form.controls['func_agregada'].value) {
      request.order_by = {
        [tableName]: [
          form.controls.aggsParam.value,
          form.controls.orderBy.value
        ]
      }
    } else {
      request.func_agregada = {
        [tableName]: [
          form.controls.aggsParam.value,
          form.controls.func_agregada.value
        ]
      }
    }

    return request;
  }

  // Função utilizada para formatar os dados de ordenação e agregação
  formatData(request: any, form: any) {
    switch(form.controls.selectedAggsTable.value) {
      case "Events":
        return request = this.addRequestInfo(request, form, "events");

      case "Classifications":
        return request = this.addRequestInfo(request, form, "classifications");
      
      case "Venues":
        return request = this.addRequestInfo(request, form, "venues");
      
      case "Attractions":
        return request = this.addRequestInfo(request, form, "attractions");
    
    }

    return request;
  }
}